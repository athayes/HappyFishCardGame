from flask import Flask, json
from flask import request
import HappySushiFunGame as fish
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
        Lobby.game.start_round()

@app.route('/StartGame', methods=['POST'])
def start_game():
    Lobby.start_game()
    
    return Lobby.game.player_json()

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
    return Lobby.game.player_json()

@app.route('/GetPlayersInLobby', methods=['POST'])
def get_players_in_lobby():
    return json.dumps({'players': Lobby.players})

@app.route('/JoinGame', methods=['POST'])
def join():
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
    
@app.route('/GetPlayersChosen', methods=['GET'])
def get_all_chosen():
    all_chosen = True
    for player in Lobby.game.players:
        all_chosen = all_chosen and Lobby.game.players.get(player).chosen
    return json.dumps(all_chosen)
    
@app.route('/PickCard', methods=['POST'])
def pick_card():
    player = request.json["playerName"]
    cardIndex = request.json["index"]
    Lobby.game.players.get(player).play(cardIndex)
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}