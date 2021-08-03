import numpy as np

from src.cards import sashimi
from src.player import ReportEntry


def score_sashimi(player):
    count = 0
    indices = []
    for index, card in enumerate(player.tableau):
        if card == sashimi:
            count += 1
            indices.append(index)
    score = get_score_for_sashimi_count(count)
    player.score += score
    if score < 0:
        player.score_report.report_entries.append(ReportEntry(f'Sashimi * {count}', score))
    player.tableau = list(np.delete(player.tableau, indices))
    return player

def get_score_for_sashimi_count(count):
    return 10 * (count//3)
