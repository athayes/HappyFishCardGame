from src.cards import ice_cream
from src.deck import make_deck
from src.player import make_players
from src.scoring_functions.dessert.ice_cream import score_ice_cream


def test_score_ice_cream_less_than_4():
    players = make_players(["bob"])
    players[0].dessert = make_deck([(ice_cream, 3)])
    players = score_ice_cream(players)
    assert players[0].score == 0
    assert len(players[0].score_report.report_entries) == 0


def test_score_ice_cream_4_or_more():
    players = make_players(["bob"])
    players[0].dessert = make_deck([(ice_cream, 4)])
    players = score_ice_cream(players)
    assert players[0].score == 12
    assert len(players[0].score_report.report_entries) == 1

