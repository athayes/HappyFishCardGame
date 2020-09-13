from flask import Flask
from flask import request
import HappySushiFunGame as fish
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

game_id = None

@app.route('/startGame', methods=['POST'])
def start_game():
    fish.Feck_It.start_game(game_id)

# Recreate game 1
@app.route('/creategame', methods=['POST'])
def create_game():
    player = request.json['player']
    game_id = fish.Feck_It.add_game()
    fish.Feck_It.add_player(player, game_id)
    return game_id

@app.route('/joingame', methods=['POST'])
def join():
    if game_id != null:
        player = request.json['player']
        fish.Feck_It.add_player(player, game_id)
    else:
        return 'You have to create a game first!'