from src import game
from src.deck import basic_deck

class Lobby:
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

    @staticmethod
    def get_game_state():
        if Lobby.game:
            return Lobby.game.game_state
        return "NOT_STARTED"
