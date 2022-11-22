from src.cards import dumpling
from src.player import Player
from src.scoring_functions.dumplings import score_dumplings


def test_score_dumpling():
    player = Player("Jen")
    player.tableau = [dumpling]
    player = score_dumplings(player)
    assert player.score == 1


def test_score_dumpling_6():
    player = Player("Jen")
    player.tableau = [dumpling, dumpling, dumpling, dumpling, dumpling, dumpling]
    player = score_dumplings(player)
    assert player.score == 15


def test_score_dumpling_score_reports():
    player = Player("Jen")
    player.tableau = [dumpling, dumpling, dumpling, dumpling, dumpling, dumpling]
    player = score_dumplings(player)
    assert player.score_report.report_entries[0].description == 'Dumplings x 6'
    assert player.score_report.report_entries[0].score == 15

def test_score_dumpling_none():
    player = Player("Jen")
    player.tableau = []
    player = score_dumplings(player)
    assert len(player.score_report.report_entries) == 0
    assert player.score == 0
