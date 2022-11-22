import numpy as np

from src.cards import tempura
from src.player import ReportEntry


def score_tempura(player):
    count = 0
    indices = []
    for index, card in enumerate(player.tableau):
        if card == tempura:
            count += 1
            indices.append(index)
    score = get_score_for_tempura_count(count)
    player.score += score
    if count > 0:
        player.score_report.report_entries.append(ReportEntry(f'Tempura x {count}', score))
    player.tableau = list(np.delete(player.tableau, indices))
    return player

def get_score_for_tempura_count(count):
    return 5 * (count//2)
