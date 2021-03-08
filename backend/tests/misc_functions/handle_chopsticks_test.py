from src.cards import chopsticks, egg_nigiri, salmon_nigiri, dumpling
from src.misc_functions.handle_chopsticks import handle_chopsticks
from src.player import Player


def test_handle_chopsticks():
    player = make_test_player()
    player = handle_chopsticks(player, 0)
    assert len(player.hand) == 2
    assert player.hand[1] == chopsticks
    assert len(player.tableau) == 1
    assert player.tableau[0] == egg_nigiri

def make_test_player():
    player = Player("Jen")
    player.hand = [egg_nigiri, salmon_nigiri]
    player.tableau = [chopsticks]
    return player