import numpy as np

from src.cards import is_maki, get_maki_number
from src.player import ReportEntry


def score_maki(players):
    players = find_maki_totals(players)
    maki_order = sorted(players, key=lambda x: x.maki_count, reverse=True)
    first_place = maki_order[0].maki_count
    second_place = maki_order[1].maki_count

    if len(players) < 6:
        for player in players:
            if player.maki_count == first_place and first_place != 0:
                player.score += 6
                player.score_report.report_entries.append(
                    ReportEntry(f'Maki: First place with {player.maki_count}', 6)
                )
            if player.maki_count == second_place and second_place != 0:
                player.score += 3
                player.score_report.report_entries.append(
                    ReportEntry(f'Maki: Second place with {player.maki_count}', 3)
                )
            # clean up
            player.maki_count = 0
    else:
        third_place = maki_order[2].maki_count
        for player in players:
            if player.maki_count == first_place and first_place != 0:
                player.score += 6
                player.score_report.report_entries.append(
                    ReportEntry(f'Maki: First place with {player.maki_count}', 6)
                )
            if player.maki_count == second_place and second_place != 0:
                player.score += 4
                player.score_report.report_entries.append(
                    ReportEntry(f'Maki: Second place with {player.maki_count}', 4)
                )
            if player.maki_count == third_place and third_place != 0:
                player.score += 2
                player.score_report.report_entries.append(
                    ReportEntry(f'Maki: Third place with {player.maki_count}', 2)
                )
            # clean up
            player.maki_count = 0

    return players


def find_maki_totals(old_players):
    players = old_players
    for player_ind, player in enumerate(players):
        maki_count = 0
        card_indices = []
        for card_ind, card in enumerate(player.tableau):
            if is_maki(card):
                maki_count += get_maki_number(card)
                card_indices.append(card_ind)
        player.maki_count = maki_count
        # remove the cards from the player's tableau
        player.tableau = list(np.delete(player.tableau, card_indices))
    return players
