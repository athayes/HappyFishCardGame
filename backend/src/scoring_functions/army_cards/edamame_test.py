from src.cards import edamame
from src.deck import make_deck
from src.player import make_players
from src.scoring_functions.army_cards.edamame import find_edamame_totals, score_edamame


def test_player_find_edamame_totals():
    players = make_test_players()
    players = find_edamame_totals(players)
    assert players[0].edamame_count == 3
    assert players[1].edamame_count == 2
    assert players[2].edamame_count == 1


def test_score_edamame():
    players = make_test_players()
    players = score_edamame(players)
    assert players[0].score == 6
    assert players[1].score == 4
    assert players[2].score == 2


def make_test_players():
    players = make_players(["P_Zero", "P_One", "P_Two"])
    players[0].tableau = make_deck([(edamame, 3)])
    players[1].tableau = make_deck([(edamame, 2)])
    players[2].tableau = make_deck([(edamame, 1)])
    return players
