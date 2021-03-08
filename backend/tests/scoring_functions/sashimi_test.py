from src.cards import sashimi
from src.deck import make_deck
from src.player import Player
from src.scoring_functions.sashimi import score_sashimi
from src.scoring_functions.tempura import score_tempura


def test_score_sashimi():
    player = Player("Jen")
    player.tableau = make_deck([(sashimi, 3)])
    player = score_sashimi(player)
    assert player.score == 10


def test_score_sashimi_7():
    player = Player("Jen")
    player.tableau = make_deck([(sashimi, 7)])
    player = score_sashimi(player)
    assert player.score == 20