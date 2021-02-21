from card_names import maki_1, maki_2, maki_3
from decks import make_deck
from scoring import score_maki, find_maki_counts
from simple_fish import make_players


def make_test_players():
    players = make_players(["P_Zero", "P_One", "P_Two", "P_Three"])
    players[0].tableau = make_deck([(maki_3, 3)])
    players[1].tableau = make_deck([(maki_2, 3)])
    players[2].tableau = make_deck([("Sashimi", 3)])
    return players


def test_find_maki_counts():
    players = make_test_players()
    players = find_maki_counts(players)
    assert players[0].maki_count == 9
    assert len(players[0].tableau) == 0
    assert players[1].maki_count == 6
    assert len(players[1].tableau) == 0
    assert len(players[2].tableau) == 3


def test_score_maki():
    players = make_test_players()
    players = score_maki(players)
    assert players[0].score == 6
    assert players[1].score == 3
