from src import game
from src.deck import basic_deck

class Lobby:
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
        Lobby.game = game.Game(Lobby.players, basic_deck(), 1)
        Lobby.is_game_started = True
