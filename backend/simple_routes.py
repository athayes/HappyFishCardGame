import random

from eventlet import sleep
from flask import Flask, json
from flask import request
from flask_cors import CORS
from flask_socketio import SocketIO, emit

from src.lobby import Lobby

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", async_handlers=True)

if __name__ == '__main__':
    socketio.run(app)

@socketio.on('connect')
def connect():
    socketio.emit('timer', {"timer": 1})


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

    if player_name in Lobby.players:
        return 'Name taken; pick a new name!'
    if Lobby.game is None:
        Lobby.add_player(player_name, is_ai)
        return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}
    return 'You have to create a game first!'


@app.route('/GetPlayers', methods=['POST'])
def get_state():
    return Lobby.game.players.get(Lobby.players[0]).to_json()


@app.route('/PickCard', methods=['POST'])
def pick_card():
    player = request.json["playerName"]
    card_index = request.json["index"]
    Lobby.game.handle_ai()
    Lobby.game.play_card(player, card_index)
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
