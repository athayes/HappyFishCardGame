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
        self.score_report = ScoreReport()

    def to_json(self):
        return {
            'player_name': self.player_name,
            'score': self.score,
            'tableau': self.tableau,
            'dessert': self.dessert,
            'hand': self.hand,
            'is_ai': self.is_ai,
            'is_new_round': self.is_new_round,
            'chosen': self.chosen,
            'score_report': self.score_report.to_json()
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


class ScoreReport:
    def __init__(self):
        self.report_entries = []
        self.tableau = []
        self.dessert = []
        self.score_round_start = 0
        self.score_round_end = 0

    def to_json(self):
        entries = []
        for entry in self.report_entries:
            entries.append(entry.to_json())
        return {
            'report_entries': entries,
            'tableau': self.tableau,
            'dessert': self.dessert,
            'score_round_start': self.score_round_start,
            'score_round_end': self.score_round_end,
        }


class ReportEntry:
    def __init__(self, description, score):
        self.description = description
        self.score = score

    def to_json(self):
        return {
            'description': self.description,
            'score': self.score,
        }