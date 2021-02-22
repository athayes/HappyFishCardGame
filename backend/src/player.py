from typing import List

class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0
        self.tableau = []
        self.dessert = []
        self.hand = []
        self.chosen = False

    def to_json(self):
        return {
            'player_name': self.player_name,
            'score': self.score,
            'tableau': self.tableau,
            'dessert': self.dessert,
            'hand': self.hand
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
