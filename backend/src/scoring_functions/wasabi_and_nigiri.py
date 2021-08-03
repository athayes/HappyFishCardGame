import numpy as np

from src.cards import wasabi, is_nigiri, get_nigiri_score
from src.player import ReportEntry


def score_wasabi_and_nigiri(arg_player):
    player = arg_player
    tableau, wasabi_score, report_entries_wasabi = score_wasabi(player.tableau)
    tableau, nigiri_score, report_entries_nigiri = score_nigiri(tableau)
    player.tableau = tableau
    player.score += (wasabi_score + nigiri_score)
    player.score_report.report_entries = player.score_report.report_entries + report_entries_wasabi + report_entries_nigiri
    return player


def score_wasabi(arg_tableau):
    tableau = arg_tableau
    indices = []
    total_score = 0
    report_entries = []
    for index, card in enumerate(tableau):
        if card == wasabi:
            # find next nigiri
            for other_index, other_card in enumerate(tableau[index:]):
                if is_nigiri(other_card):
                    score = get_nigiri_score(other_card) * 3
                    total_score += score
                    indices.append(other_index)
                    # mark the card as "played" so it can't be picked up by next wasabi
                    tableau[other_index] = "played_nigiri"
                    if score > 0:
                        report_entries.append(ReportEntry(f'Wasabi + {other_card}', score))

                    break  # leave the loop, found our match
            wasabi_index = index
            indices.append(wasabi_index)

    tableau = list(np.delete(tableau, indices))
    return tableau, total_score, report_entries


def score_nigiri(arg_tableau):
    tableau = arg_tableau
    indices = []
    total_score = 0
    report_entries = []
    for index, card in enumerate(tableau):
        if is_nigiri(card):
            score = get_nigiri_score(card)
            total_score += score
            indices.append(index)
            if score > 0:
                report_entries.append(ReportEntry(card, score))

    tableau = list(np.delete(tableau, indices))
    return tableau, total_score, report_entries
