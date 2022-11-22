import numpy as np

from src.cards import eel
from src.player import ReportEntry


def score_eel(player):
    count = 0
    indices = []
    for index, card in enumerate(player.tableau):
        if card == eel:
            count += 1
            indices.append(index)
    score = get_score_for_eel_count(count)
    player.score += score
    if count > 0:
        player.score_report.report_entries.append(ReportEntry(f'Eel x {count}', score))
    player.tableau = list(np.delete(player.tableau, indices))
    return player


def get_score_for_eel_count(count):
    if count < 1:
        return 0
    if count == 1:
        return -3
    return 7
