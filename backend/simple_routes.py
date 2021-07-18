from flask import Flask, json
from flask import request
from flask_cors import CORS
from flask_socketio import SocketIO
from copy import deepcopy

from src.lobby import Lobby

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_handlers=False)


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
    Lobby.start_game()
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


@app.route('/ResetLobbyAndGame', methods=['POST'])
def reset_lobby_and_game():
    Lobby.reset_game()
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


@app.route('/CreateLobby', methods=['POST'])
def create_game():
    player_name = request.json['hostName']
    Lobby.reset_game()
    Lobby.add_player(player_name, False)
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


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
    return {
        'players': Lobby.player_json(),
        'game_state': Lobby.get_game_state()
    }


@app.route('/JoinLobby', methods=['POST'])
def join_lobby():
    player_name = request.json['playerName']
    is_ai = request.json['is_ai']
    for player in Lobby.players:
        if player_name == player.player_name:
            return 'Name taken; pick a new name!', 200
    Lobby.add_player(player_name, is_ai)
    push_lobby_data()
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


@app.route('/GetPlayers', methods=['POST'])
def get_state():
    return Lobby.game.players.get(Lobby.players[0]).to_json()


@app.route('/PickCard', methods=['POST'])
def pick_card():
    player = request.json["playerName"]
    card_index = request.json["index"]
    Lobby.game.handle_ai()
    Lobby.game.play_card(player, card_index)
    if Lobby.game.game_state == "COMPLETED":
        Lobby.last_finished_game = deepcopy(Lobby.game)
        Lobby.game = None
        Lobby.players = []
        push_game_end()
    else:
        push_game_data()
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


@app.route('/PickCardChopsticks', methods=['POST'])
def pick_card_chopsticks():
    player = request.json["playerName"]
    card_1_index = request.json["index1"]
    card_2_index = request.json["index2"]
    Lobby.game.handle_ai()
    Lobby.game.play_card_chopsticks(player, card_1_index, card_2_index)
    if Lobby.game.game_state == "COMPLETED":
        Lobby.last_finished_game = deepcopy(Lobby.game)
        Lobby.game = None
        Lobby.players = []
        push_game_end()
    else:
        push_game_data()
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


@app.route('/SetUpTestGame', methods=['POST'])
def set_up_test_game():
    Lobby.reset_game()
    Lobby.add_player("reb", False)
    Lobby.add_player("Cool H", False)
    Lobby.start_game()
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


@app.route('/CanPlayCard', methods=['POST'])
def can_play_card():
    player = request.json["playerName"]
    return {
        "game_state": Lobby.game.game_state,
        "can_play_card": not Lobby.game.is_player_chosen(player)
    }


def push_lobby_data():
    socketio.emit("lobbyUpdates", {
        "players": Lobby.player_json(),
        "game_state": Lobby.get_game_state()
    })


def push_game_data():
    socketio.emit("gameUpdates", {
        "players": Lobby.game.player_json(),
        "game_state": Lobby.game.game_state,
        "round": Lobby.game.round
    })


def push_game_end():
    socketio.emit("gameUpdates", {
        "players": Lobby.last_finished_game.player_json(),
        "game_state": Lobby.last_finished_game.game_state,
        "round": Lobby.last_finished_game.round
    })
