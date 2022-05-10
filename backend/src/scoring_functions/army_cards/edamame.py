import numpy as np

from src.cards import edamame
from src.player import ReportEntry


def score_edamame(players):
    players = find_edamame_totals(players)
    players_with_edamame = 0
    for player in players:
        if player.edamame_count > 0:
            players_with_edamame += 1
    if players_with_edamame >= 2:
        for player in players:
            score = min(4, players_with_edamame - 1) * player.edamame_count
            player.score += score
            player.score_report.report_entries.append(
                ReportEntry(f'Edamame: {player.edamame_count}', score)
            )
    return players


def find_edamame_totals(players):
    for player_ind, player in enumerate(players):
        edamame_count = 0
        card_indices = []
        for card_ind, card in enumerate(player.tableau):
            if card == edamame:
                edamame_count += 1
                card_indices.append(card_ind)
        player.edamame_count = edamame_count
        # remove the cards from the player's tableau
        player.tableau = list(np.delete(player.tableau, card_indices))
    return players
