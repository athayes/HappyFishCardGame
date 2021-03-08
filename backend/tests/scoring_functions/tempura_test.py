from src.cards import tempura
from src.deck import make_deck
from src.player import Player
from src.scoring_functions.tempura import score_tempura


def test_score_tempura():
    player = Player("Jen")
    player.tableau = make_deck([(tempura, 2)])
    player = score_tempura(player)
    assert player.score == 5


def test_score_tempura_7():
    player = Player("Jen")
    player.tableau = make_deck([(tempura, 7)])
    player = score_tempura(player)
    assert player.score == 15
