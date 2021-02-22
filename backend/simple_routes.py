from flask import Flask, json

from flask import request
from flask_cors import CORS

from src import game
from src.deck import basic_deck

app = Flask(__name__)
CORS(app)


class Lobby:
    host_name = None
    is_game_started = False
    game = None
    players = []

    @staticmethod
    def add_player(player_name):
        Lobby.players.append(player_name)

    @staticmethod
    def reset_game():
        Lobby.game = None
        Lobby.players = []

    @staticmethod
    def start_game():
        Lobby.game = game.Game(Lobby.players, basic_deck(), 3)
        Lobby.is_game_started = True


@app.route('/StartGame', methods=['POST'])
def start_game():
    Lobby.start_game()
    return Lobby.game.player_json()


@app.route('/CreateLobby', methods=['POST'])
def create_game():
    player_name = request.json['hostName']
    Lobby.reset_game()
    Lobby.add_player(player_name)
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


@app.route('/GetGameObject', methods=['POST'])
def get_game_object():
    return {
        "players": Lobby.game.player_json(),
        "round": Lobby.game.round
    }


@app.route('/GetLobby', methods=['POST'])
def get_lobby():
    return {
        'players': Lobby.players,
        'host_name': Lobby.host_name,
        'is_game_started': Lobby.is_game_started
    }


@app.route('/JoinLobby', methods=['POST'])
def join_lobby():
    player_name = request.json['playerName']
    if player_name in Lobby.players:
        return 'Name taken; pick a new name!'
    if Lobby.game is None:
        Lobby.add_player(player_name)
        return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}
    return 'You have to create a game first!'


@app.route('/GetPlayers', methods=['POST'])
def get_state():
    return Lobby.game.players.get(Lobby.players[0]).to_json()


@app.route('/PickCard', methods=['POST'])
def pick_card():
    player = request.json["playerName"]
    card_index = request.json["index"]
    Lobby.game.play_card(player, card_index)
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


@app.route('/SetUpTestGame', methods=['POST'])
def set_up_test_game():
    Lobby.reset_game()
    Lobby.add_player("reb")
    Lobby.add_player("Cool H")
    Lobby.host_name = "reb"
    Lobby.start_game()
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


@app.route('/CanPlayCard', methods=['POST'])
def can_play_card():
    player = request.json["playerName"]
    return {
        "canPlayCard": not Lobby.game.is_player_chosen(player)
    }
