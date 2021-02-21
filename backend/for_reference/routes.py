from flask import Flask, json
from flask import request
from for_reference import HappySushiFunGame as fish
from flask_cors import CORS

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
        Lobby.game = fish.Game(Lobby.players)
        Lobby.game.start_round()
        Lobby.is_game_started = True

@app.route('/StartGame', methods=['POST'])
def start_game():
    Lobby.start_game()
    
    return Lobby.game.player_json()

# Recreate game 1
@app.route('/CreateLobby', methods=['POST'])
def create_game():
    host_name = request.json['hostName']
    Lobby.reset_game()
    Lobby.add_player(host_name)
    Lobby.host_name = host_name
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}


# Recreate game 1
@app.route('/GetGameObject', methods=['POST'])
def get_game_object():
    return {
        "players": Lobby.game.player_json()
    }

@app.route('/GetLobby', methods=['POST'])
def get_players_in_lobby():
    return {'players': Lobby.players,
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
    
@app.route('/GetPlayersChosen', methods=['POST'])
def get_all_chosen():
    all_chosen = Lobby.game.check_all_players_chosen()
    return json.dumps({"all_chosen" : all_chosen })
    
@app.route('/PickCard', methods=['POST'])
def pick_card():
    player = request.json["playerName"]
    cardIndex = request.json["index"]
    Lobby.game.players.get(player).play(cardIndex)

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
def get_player_chosen():
    player = request.json["playerName"]
    return {
        "canPlayCard": not Lobby.game.players.get(player).chosen
    }
