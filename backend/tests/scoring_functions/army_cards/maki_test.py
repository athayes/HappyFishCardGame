from src.cards import maki_2, maki_3
from src.deck import make_deck
from src.scoring_functions.army_cards.maki import score_maki, find_maki_totals
from src.player import make_players


def test_player_find_maki_totals():
    players = make_test_players()
    players = find_maki_totals(players)
    assert players[0].maki_count == 9
    assert len(players[0].tableau) == 0
    assert players[1].maki_count == 6
    assert len(players[1].tableau) == 0
    assert len(players[2].tableau) == 3


def test_score_maki():
    players = make_test_players()
    players = score_maki(players)
    assert players[0].score == 6
    assert players[0].score_report.report_entries[0].description == 'Maki: First place with 9'
    assert players[0].score_report.report_entries[0].score == 6
    assert players[1].score == 3
    assert players[1].score_report.report_entries[0].description == 'Maki: Second place with 6'
    assert players[1].score_report.report_entries[0].score == 3

# Is broke pls fix
# def test_score_maki_2():
#     players = make_players(["P_Zero", "P_One", "P_Two", "P_Three"])
#     players[0].tableau = make_deck([(maki_2, 1)])
#     players[1].tableau = make_deck([(maki_2, 2)])
#     players = score_maki(players)
#     assert players[0].score == 3
#     assert players[0].score_report.report_entries[0].description == 'Maki: First place with 9'
#     assert players[0].score_report.report_entries[0].score == 3
#     assert players[1].score == 6
#     assert players[1].score_report.report_entries[0].description == 'Maki: Second place with 6'
#     assert players[1].score_report.report_entries[0].score == 6


def make_test_players():
    players = make_players(["P_Zero", "P_One", "P_Two", "P_Three"])
    players[0].tableau = make_deck([(maki_3, 3)])
    players[1].tableau = make_deck([(maki_2, 3)])
    players[2].tableau = make_deck([("Sashimi", 3)])
    return players
