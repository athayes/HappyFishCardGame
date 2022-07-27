from src.cards import eel
from src.deck import make_deck
from src.player import Player
from src.scoring_functions.eel import score_eel


def test_score_no_eel():
    player = Player("Jen")
    player.tableau = make_deck([(eel, 0)])
    player = score_eel(player)
    assert player.score == 0


def test_score_1_eel():
    player = Player("Jen")
    player.tableau = make_deck([(eel, 1)])
    player = score_eel(player)
    assert player.score == -3


def test_score_2_eel():
    player = Player("Jen")
    player.tableau = make_deck([(eel, 2)])
    player = score_eel(player)
    assert player.score == 7
