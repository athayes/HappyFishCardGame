import numpy as np
from src.cards import pudding
from src.player import ReportEntry


def score_pudding(players):
    players = find_pudding_totals(players)
    first_place = 0
    last_place = players[0].pudding_count
    for player in players:
        if player.pudding_count > first_place:
            first_place = player.pudding_count
        elif player.pudding_count < last_place:
            last_place = player.pudding_count

    if first_place == last_place:
        return players

    for player in players:
        if player.pudding_count == first_place:
            player.score += 6
            player.score_report.report_entries.append(
                ReportEntry(f'Pudding: First place with {player.pudding_count}', 6)
            )
        if player.pudding_count == last_place:
            if len(players) != 2:
                player.score -= 6
                player.score_report.report_entries.append(
                    ReportEntry(f'Pudding: Last place with {player.pudding_count}', -6)
                )
        player.pudding_count = 0
    return players


def find_pudding_totals(players):
    for player_ind, player in enumerate(players):
        pudding_count = 0
        card_indices = []
        for card_ind, card in enumerate(player.dessert):
            if card == pudding:
                pudding_count += 1
                card_indices.append(card_ind)
        player.pudding_count = pudding_count
        # remove the cards from the player's dessert
        player.dessert = list(np.delete(player.dessert, card_indices))
    return players
