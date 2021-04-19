from typing import List

class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0
        self.tableau = []
        self.dessert = []
        self.hand = []
        self.chosen = False
        self.is_ai = False
        self.is_new_round = False

    def to_json(self):
        return {
            'player_name': self.player_name,
            'score': self.score,
            'tableau': self.tableau,
            'dessert': self.dessert,
            'hand': self.hand,
            'is_ai': self.is_ai,
            'is_new_round': self.is_new_round,
            'chosen': self.chosen
        }

def make_players(player_names) -> List[Player]:
    players = []
    for player_name in player_names:
        players.append(Player(player_name))
    return players

def find_player(player_name, players) -> (int, Player):
    for index, player in enumerate(players):
        if player.player_name == player_name:
            return index, player
    raise ValueError("player not found in list")


def mark_new_round(players: List[Player], is_new_round):
    for player in players:
        player.is_new_round = is_new_round
    return players
