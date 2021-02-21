from src.cards import egg_nigiri, salmon_nigiri, squid_nigiri, wasabi, maki_1
from src.player import Player
from src.scoring_functions.wasabi_and_nigiri import score_nigiri, score_wasabi, \
    score_wasabi_and_nigiri


def test_score_egg_nigiri():
    tableau, score = score_nigiri([egg_nigiri])
    assert score == 1

def test_score_salmon_nigiri():
    tableau, score = score_nigiri([salmon_nigiri])
    assert score == 2
    assert len(tableau) == 0

def test_score_squid_nigiri():
    tableau, score = score_nigiri([squid_nigiri])
    assert score == 3
    assert len(tableau) == 0

def test_score_wasabi_egg():
    tableau, score = score_wasabi([wasabi, egg_nigiri])
    assert score == 3
    assert len(tableau) == 0

def test_score_wasabi_egg_plus_nigiri():
    tableau, score = score_wasabi([wasabi, egg_nigiri, egg_nigiri])
    assert len(tableau) == 1
    assert tableau[0] == egg_nigiri
    assert score == 3

def test_score_wasabi_salmon():
    tableau, score = score_wasabi([wasabi, salmon_nigiri])
    assert score == 6

def test_score_wasabi_squid():
    tableau, score = score_wasabi([wasabi, squid_nigiri])
    assert score == 9

def test_score_wasabi_and_nigiri():
    player = Player("test_player")
    player.tableau = [wasabi, squid_nigiri, egg_nigiri]
    player = score_wasabi_and_nigiri(player)
    assert player.score == 10


def test_score_wasabi_and_nigiri_2():
    player = Player("test_player")
    player.tableau = [wasabi, squid_nigiri, maki_1]
    player = score_wasabi_and_nigiri(player)
    assert player.score == 9