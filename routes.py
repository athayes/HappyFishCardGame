from flask import Flask
from flask import request
app = Flask(__name__)

games = {}

@app.route('/play', methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        Game g = new Game()
        games[g.id] = g
    return 'Welcome Page'

@app.route('/games/', methods=['GET'])
def games():
    return 'Index Page'

@app.route('/games/<game_id>', methods=['GET', 'DELETE'])
def show_game():
    return 'Game %d' % game_id

@app.route('/players/', methods=['GET'])
def players():
    return 'Index Page'

@app.route('/players/<player_id>', methods=['GET', 'DELETE'])
def show_player():
    return jsonify({})