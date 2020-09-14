
from flask import Flask, json
from flask import request
import HappySushiFunGame as fish
from flask_cors import CORS

game_id = None
app = Flask(__name__)
CORS(app)

@app.route('/StartGame', methods=['POST'])
def start_game():
    fish.Feck_It.start_game(game_id)

# Recreate game 1
@app.route('/CreateGame', methods=['POST'])
def create_game():
    hostName = request.json['hostName']
    fish.Feck_It.reset_game()
    fish.Feck_It.add_player(hostName)
    return json.dumps(dict(success=True)), 200, {'ContentType': 'application/json'}

# Recreate game 1
@app.route('/GetGameObject', methods=['POST'])
def get_game_object():
    return fish.Feck_It.game

@app.route('/JoinGame', methods=['POST'])
def join():
    if game_id != null:
        player = request.json['player']
        fish.Feck_It.add_player(player, game_id)
    else:
        return 'You have to create a game first!'