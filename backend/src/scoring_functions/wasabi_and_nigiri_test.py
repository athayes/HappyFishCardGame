from src.cards import egg_nigiri, salmon_nigiri, squid_nigiri, wasabi, maki_1
from src.player import Player
from src.scoring_functions.wasabi_and_nigiri import score_nigiri, score_wasabi, \
    score_wasabi_and_nigiri


def test_score_egg_nigiri():
    tableau, score, report_entries = score_nigiri([egg_nigiri])
    assert score == 1


def test_score_salmon_nigiri():
    tableau, score, report_entries = score_nigiri([salmon_nigiri])
    assert score == 2
    assert len(tableau) == 0


def test_score_squid_nigiri():
    tableau, score, report_entries = score_nigiri([squid_nigiri])
    assert score == 3
    assert len(tableau) == 0


def test_score_wasabi_egg():
    tableau, score, report_entries = score_wasabi([wasabi, egg_nigiri])
    assert score == 3
    assert len(tableau) == 0


def test_score_wasabi_egg_plus_nigiri():
    tableau, score, report_entries = score_wasabi([wasabi, egg_nigiri, egg_nigiri])
    assert len(tableau) == 1
    assert tableau[0] == egg_nigiri
    assert score == 3


def test_score_wasabi_salmon():
    tableau, score, report_entries = score_wasabi([wasabi, salmon_nigiri])
    assert score == 6


def test_score_wasabi_squid():
    tableau, score, report_entries = score_wasabi([wasabi, squid_nigiri])
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


def test_score_two_wasabi():
    player = Player("test_player")
    player.tableau = [wasabi, wasabi, egg_nigiri]
    player = score_wasabi_and_nigiri(player)
    assert player.score == 3
    assert len(player.tableau) == 0


def test_many_dupes():
    player = Player("test_player")
    player.tableau = [egg_nigiri, egg_nigiri, egg_nigiri, egg_nigiri]
    player = score_wasabi_and_nigiri(player)
    assert player.score == 4
    assert len(player.score_report.report_entries) == 1
    assert player.score_report.report_entries[0].description == f'Egg Nigiri x 4'
    assert player.score_report.report_entries[0].score == 4
    assert len(player.tableau) == 0


def test_many_wasabi_combo():
    player = Player("test_player")
    player.tableau = [wasabi, egg_nigiri, wasabi, egg_nigiri]
    player = score_wasabi_and_nigiri(player)
    assert player.score == 6
    assert len(player.score_report.report_entries) == 1
    assert player.score_report.report_entries[0].description == f'Wasabi and Egg Nigiri x 2'
    assert player.score_report.report_entries[0].score == 6
    assert len(player.tableau) == 0


def test_wasabi_order():
    player = Player("test_player")
    player.tableau = [egg_nigiri, wasabi, egg_nigiri, wasabi]
    player = score_wasabi_and_nigiri(player)
    assert player.score == 4
    assert len(player.tableau) == 0
