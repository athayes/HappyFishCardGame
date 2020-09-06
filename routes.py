from flask import Flask
from flask import request
import HappySushiFunGame as fish
app = Flask(__name__)

game = null

@app.route('/startGame', methods=['POST'])
def start():
    game.start()

# Recreate game 1
@app.route('/creategame', methods=['POST'])
def games():
    play = pass #Get player from POST
    game = new fish.Game()
    game.addPlayer(player)
    return game

@app.route('/joingame', methods=['POST'])
def join():
    if game != null:
        play = pass #Get player from POST
        game.addPlayer(player)
    else:
        return 'You have to create a game first!'