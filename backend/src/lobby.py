from copy import deepcopy

from src import game
from src.deck import basic_deck
from src.names import upstanding_name
from src.player import Player


class Lobby:
    def __init__(self):
        self.game_starting = False
        self.game = None
        self.last_finished_game = None
        self.players = []
        self.deck, self.dessert = basic_deck()

    def add_player(self, player_name, is_ai):
        if is_ai:
            player_name = upstanding_name(self.players)
        player = Player(player_name)
        player.is_ai = is_ai
        self.players.append(player)

    def reset_game(self):
        self.game_starting = False
        self.game = None
        self.players = []

    def start_game(self):
        if not self.game_starting:
            self.game_starting = True
            self.game = game.Game(deepcopy(self.players), self.deck, self.dessert, 10)

    def get_game_state(self):
        if self.game:
            return self.game.game_state
        return "NOT_STARTED"

    def player_json(self):
        data = []
        for player in self.players:
            data.append(player.to_json())
        return data

    def last_finished_game_to_json(self):
        return {
            'game_state': self.last_finished_game.game_state,
            'round': self.last_finished_game.round,
            'deck': self.last_finished_game.deck,
            "players": self.last_finished_game.player_json()
        }
