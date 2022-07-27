import numpy as np

from src.cards import temaki
from src.player import ReportEntry


def score_temaki(players):
    players, in_play = find_temaki_totals(players)
    if not in_play:
        return players

    temaki_order = sorted(players, key=lambda x: x.temaki_count, reverse=True)
    first_place = temaki_order[0].temaki_count
    last_place = temaki_order[-1].temaki_count
    for player in players:
        if player.temaki_count == first_place and first_place != 0:
            player.score += 4
            player.score_report.report_entries.append(
                ReportEntry(f'Temaki: First place with {player.temaki_count}', 4)
            )
        if len(players) > 2:
            if player.temaki_count == last_place:
                player.score -= 4
            player.score_report.report_entries.append(
                ReportEntry(f'Temaki: Second place with {player.temaki_count}', -4)
            )
        # clean up
        player.temaki_count = 0
    return players


def find_temaki_totals(players):
    in_play = False
    for player_ind, player in enumerate(players):
        temaki_count = 0
        card_indices = []
        for card_ind, card in enumerate(player.tableau):
            if card == temaki:
                in_play = True
                temaki_count += 1
                card_indices.append(card_ind)
        player.temaki_count = temaki_count
        # remove the cards from the player's tableau
        player.tableau = list(np.delete(player.tableau, card_indices))
    return players, in_play
