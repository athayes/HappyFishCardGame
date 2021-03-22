from src import game
from src.deck import basic_deck
from src.player import Player


class Lobby:
    game = None
    players = []

    @staticmethod
    def add_player(player_name, is_ai):
        player = Player(player_name)
        player.is_ai = is_ai
        Lobby.players.append(player)

    @staticmethod
    def reset_game():
        Lobby.game = None
        Lobby.players = []

    @staticmethod
    def start_game():
        Lobby.game = game.Game(Lobby.players, basic_deck(), 10)

    @staticmethod
    def get_game_state():
        if Lobby.game:
            return Lobby.game.game_state
        return "NOT_STARTED"

    @staticmethod
    def player_json():
        data = []
        for player in Lobby.players:
            data.append(player.to_json())
        return data
