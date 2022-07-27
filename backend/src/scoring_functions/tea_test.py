from src.cards import sashimi, tea, squid_nigiri, tempura
from src.deck import make_deck
from src.player import Player
from src.scoring_functions.tea import score_tea


def test_score_tea():
    player = Player("Jen")
    player.tableau = make_deck([(sashimi, 3), (tea, 1)])
    player = score_tea(player)
    assert player.score == 3
    assert len(player.tableau) == 3


def test_score_tea_mixed():
    player = Player("Jen")
    player.tableau = make_deck([(sashimi, 1), (squid_nigiri, 2), (tempura, 5), (tea, 1)])
    player = score_tea(player)
    assert player.score == 5
    assert len(player.tableau) == 8
