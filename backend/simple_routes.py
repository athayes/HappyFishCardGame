from flask import Flask, json
from flask import request
from flask_cors import CORS
from flask_socketio import SocketIO
from copy import deepcopy

from src.deck import custom_deck
from src.lobby import Lobby
import uuid

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_handlers=False)

Lobbies = {}


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/', methods=['GET'])
def root():
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


@app.route('/StartGame', methods=['POST'])
def start_game():
    lobby_id = request.json['lobbyId']
    lobby = Lobbies[lobby_id]
    lobby.start_game()
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


@app.route('/ResetLobbyAndGame', methods=['POST'])
def reset_lobby_and_game():
    lobby_id = request.json['lobbyId']
    lobby = Lobbies[lobby_id]
    lobby.reset_game()
    push_lobby_data(lobby_id)
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


@app.route('/CreateLobby', methods=['POST'])
def create_game():
    player_name = request.json['name']
    lobby_id = str(uuid.uuid4())
    Lobbies[lobby_id] = Lobby()
    Lobbies[lobby_id].add_player(player_name, False)
    return {
        "lobbyId": lobby_id
    }


@app.route('/GetGameObject', methods=['POST'])
def get_game_object():
    return {
        "game_state": Lobby.game.game_state,
        "players": Lobby.game.player_json(),
        "round": Lobby.game.round
    }


@app.route('/GetLastFinishedGameObject', methods=['POST'])
def get_last_finished_game_object():
    return {
        "game_state": Lobby.last_finished_game.game_state,
        "players": Lobby.last_finished_game.player_json(),
        "round": Lobby.last_finished_game.round
    }


@app.route('/GetLobby', methods=['POST'])
def get_lobby():
    lobby_id = request.json['lobbyId']
    print(lobby_id)
    print(Lobbies)
    lobby = Lobbies[lobby_id]
    return {
        'players': lobby.player_json(),
        'game_state': lobby.get_game_state()
    }


@app.route('/JoinLobby', methods=['POST'])
def join_lobby():
    lobby_id = request.json['lobbyId']
    player_name = request.json['playerName']
    is_ai = request.json['is_ai']
    if len(Lobby.players) >= 8:
        return 'Too many players', 200
    for player in Lobby.players:
        if player_name == player.player_name:
            return 'Name taken; pick a new name!', 200
    Lobbies[lobby_id].add_player(player_name, is_ai)
    push_lobby_data(lobby_id)
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


@app.route('/GetPlayers', methods=['POST'])
def get_state():
    return Lobby.game.players.get(Lobby.players[0]).to_json()


@app.route('/PickCard', methods=['POST'])
def pick_card():
    lobby_id = request.json["lobbyId"]
    player = request.json["playerName"]
    card_index = request.json["index"]
    Lobby.game.handle_ai()
    Lobby.game.play_card(player, card_index)
    # Todo investigate possible race condition
    if Lobby.game.game_state == "COMPLETED":
        Lobby.last_finished_game = deepcopy(Lobby.game)
        Lobby.game_starting = False
        Lobby.game = None
        Lobby.players = []
        push_game_end(lobby_id)
    else:
        push_game_data(lobby_id)
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


@app.route('/PickCardChopsticks', methods=['POST'])
def pick_card_chopsticks():
    lobby_id = request.json["lobbyId"]
    player = request.json["playerName"]
    card_1_index = request.json["index1"]
    card_2_index = request.json["index2"]
    Lobby.game.handle_ai()
    Lobby.game.play_card_chopsticks(player, card_1_index, card_2_index)
    if Lobby.game.game_state == "COMPLETED":
        Lobby.last_finished_game = deepcopy(Lobby.game)
        Lobby.game = None
        Lobby.players = []
        push_game_end(lobby_id)
    else:
        push_game_data(lobby_id)
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


def push_lobby_data(lobby_id):
    lobby = Lobbies[lobby_id]
    socketio.emit(
        "lobbyUpdates",
        {
            "players": lobby.player_json(),
            "game_state": lobby.get_game_state()
        },
        room=lobby_id,
    )


def push_game_data(lobby_id):
    lobby = Lobbies[lobby_id]
    socketio.emit(
        "gameUpdates",
        {
            "players": lobby.game.player_json(),
            "game_state": lobby.game.game_state,
            "round": lobby.game.round
        },
        room=lobby_id,
    )


def push_game_end(lobby_id):
    lobby = Lobbies[lobby_id]
    socketio.emit(
        "gameUpdates",
        {
            "players": lobby.last_finished_game.player_json(),
            "game_state": lobby.last_finished_game.game_state,
            "round": lobby.last_finished_game.round
        },
        room=lobby_id,
    )


@app.route('/PickDeck', methods=['POST'])
def pick_deck():
    print(request.json["deck"])
    Lobby.deck, Lobby.desserts = custom_deck(request.json["deck"])
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}
