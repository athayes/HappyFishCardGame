from src.cards import pudding
from src.deck import make_deck
from src.player import make_players
from src.scoring_functions.dessert.pudding import find_pudding_totals, score_pudding


def test_player_find_pudding_totals():
    players = make_players(["P_Zero", "P_One", "P_Two", "P_Three"])
    players[0].dessert = make_deck([(pudding, 3)])
    players[1].dessert = make_deck([(pudding, 2)])
    players[2].dessert = make_deck([("Sashimi", 3)])
    players = find_pudding_totals(players)
    assert players[0].pudding_count == 3
    assert len(players[0].dessert) == 0
    assert players[1].pudding_count == 2
    assert len(players[1].dessert) == 0
    assert len(players[2].dessert) == 3


def test_score_pudding_2_player():
    players = make_players(["P_Zero", "P_One"])
    players[0].dessert = make_deck([(pudding, 3)])
    players[1].dessert = make_deck([(pudding, 2)])
    players = score_pudding(players)
    assert players[0].score == 6
    assert players[1].score == 0

def test_score_pudding_3_player():
    players = make_players(["P_Zero", "P_One", "P_Two"])
    players[0].dessert = make_deck([(pudding, 3)])
    players[1].dessert = make_deck([(pudding, 0)])
    players[2].dessert = make_deck([(pudding, 1)])
    players = score_pudding(players)
    assert players[0].score == 6
    assert players[1].score == -6
    assert players[2].score == 0

def test_score_pudding_3_player_everyone_same():
    players = make_players(["P_Zero", "P_One", "P_Two"])
    players[0].dessert = make_deck([(pudding, 3)])
    players[1].dessert = make_deck([(pudding, 3)])
    players[2].dessert = make_deck([(pudding, 3)])
    players = score_pudding(players)
    assert players[0].score == 0
    assert players[1].score == 0
    assert players[2].score == 0
