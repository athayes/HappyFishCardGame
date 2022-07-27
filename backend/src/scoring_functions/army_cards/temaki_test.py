from src.cards import temaki
from src.deck import make_deck
from src.player import make_players
from src.scoring_functions.army_cards.temaki import find_temaki_totals, score_temaki


def test_player_find_temaki_totals():
    players = make_test_players()
    players = find_temaki_totals(players)
    assert players[0].temaki_count == 3
    assert players[1].temaki_count == 2
    assert players[2].temaki_count == 1


def test_score_temaki():
    players = make_test_players()
    players = score_temaki(players)
    assert players[0].score == 4
    assert players[1].score == 0
    assert players[2].score == -4


def test_score_temaki_2_player():
    players = make_test_players()
    players.pop()
    players = score_temaki(players)
    assert players[0].score == 4
    assert players[1].score == 0


def make_test_players():
    players = make_players(["P_Zero", "P_One", "P_Two"])
    players[0].tableau = make_deck([(temaki, 3)])
    players[1].tableau = make_deck([(temaki, 2)])
    players[2].tableau = make_deck([(temaki, 1)])
    return players
