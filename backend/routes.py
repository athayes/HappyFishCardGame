from flask import Flask, json
from flask import request
import HappySushiFunGame as fish
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/StartGame', methods=['POST'])
def start_game():
    Lobby.start_game()
    return json.dumps(Lobby.game.players)


# Recreate game 1
@app.route('/CreateGame', methods=['POST'])
def create_game():
    host_name = request.json['hostName']
    Lobby.reset_game()
    Lobby.add_player(host_name)
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


# Recreate game 1
@app.route('/GetGameObject', methods=['POST'])
def get_game_object():
    return json.dumps({'players': Lobby.game.players})

@app.route('/JoinGame', methods=['POST'])
def join():
    if Lobby.game is None:
        player_name = request.json['playerName']
        Lobby.add_player(player_name)
        return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}
    else:
        return 'You have to create a game first!'


class Lobby:
    game = None
    players = []

    @staticmethod
    def add_player(player_name):
        Lobby.players.append(player_name)

    @staticmethod
    def reset_game():
        Lobby.players = []

    @staticmethod
    def start_game():
        Lobby.game = fish.Game(Lobby.players)
