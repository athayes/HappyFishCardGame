from copy import deepcopy

from src import game
from src.deck import basic_deck, basic_desserts
from src.player import Player


class Lobby:
    game = None
    last_finished_game = None
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
        deck = basic_deck()
        desserts = basic_desserts()
        Lobby.game = game.Game(deepcopy(Lobby.players), deck, desserts, 10)

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

    @staticmethod
    def last_finished_game_to_json():
        return {
            'game_state': Lobby.last_finished_game.game_state,
            'round': Lobby.last_finished_game.round,
            'deck': Lobby.last_finished_game.deck,
            "players": Lobby.last_finished_game.player_json()
        }
