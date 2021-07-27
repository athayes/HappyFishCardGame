import numpy as np

from src.cards import dumpling
from src.player import ReportEntry


def score_dumplings(player):
    count = 0
    indices = []
    for index, card in enumerate(player.tableau):
        if card == dumpling:
            count += 1
            indices.append(index)
    score = get_score_for_dumpling_count(count)
    player.score += score
    player.score_report.report_entries.append(ReportEntry(f'Dumplings * {count}', score))
    player.tableau = list(np.delete(player.tableau, indices))
    return player


def get_score_for_dumpling_count(count):
    if count > 5:
        count = 5
    score_map = {0: 0, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15}
    return score_map.get(count)
