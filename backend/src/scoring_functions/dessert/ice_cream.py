import numpy as np
from src.cards import ice_cream
from src.player import ReportEntry


def score_ice_cream(players):
    for player in players:
        count = 0
        card_indices = []
        for card_ind, card in enumerate(player.dessert):
            if card == ice_cream:
                count += 1
                card_indices.append(card_ind)
        if count >= 4:
            score = 12
            player.score += score
            player.score_report.report_entries.append(ReportEntry(f'Ice Cream x {count}', score))

        player.dessert = list(np.delete(player.dessert, card_indices))
    return players
