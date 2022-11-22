import numpy as np

from src.cards import wasabi, is_nigiri, get_nigiri_score, salmon_nigiri, egg_nigiri, squid_nigiri
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
    wasabi_egg = 0
    wasabi_salmon = 0
    wasabi_squid = 0
    for index, card in enumerate(tableau):
        if card == wasabi:
            # find next nigiri
            for other_index, other_card in enumerate(tableau):
                if other_index > index and is_nigiri(other_card):
                    if other_card == egg_nigiri:
                        wasabi_egg += 1
                    if other_card == salmon_nigiri:
                        wasabi_salmon += 1
                    if other_card == squid_nigiri:
                        wasabi_squid += 1
                    indices.append(other_index)
                    # mark the card as "played" so it can't be picked up by next wasabi
                    tableau[other_index] = "played_nigiri"
                    break  # leave the loop, found our match
            wasabi_index = index
            indices.append(wasabi_index)
    if wasabi_egg > 0:
        score = get_nigiri_score(egg_nigiri) * 3 * wasabi_egg
        total_score += score
        report_entries.append(ReportEntry(f'Wasabi and Egg Nigiri x {wasabi_egg}', score))
    if wasabi_salmon > 0:
        score = get_nigiri_score(salmon_nigiri) * 3 * wasabi_salmon
        total_score += score
        report_entries.append(ReportEntry(f'Wasabi and Salmon Nigiri x {wasabi_salmon}', score))
    if wasabi_squid > 0:
        score = get_nigiri_score(squid_nigiri) * 3  * wasabi_squid
        total_score += score
        report_entries.append(ReportEntry(f'Wasabi and Squid Nigiri x {wasabi_squid}', score))

    tableau = list(np.delete(tableau, indices))
    return tableau, total_score, report_entries


def score_nigiri(arg_tableau):
    tableau = arg_tableau
    indices = []
    total_score = 0
    report_entries = []
    egg = 0
    salmon = 0
    squid = 0
    for index, card in enumerate(tableau):
        if is_nigiri(card):
            if card == egg_nigiri:
                egg += 1
            if card == salmon_nigiri:
                salmon += 1
            if card == squid_nigiri:
                squid += 1
            indices.append(index)

    if egg > 0:
        score = get_nigiri_score(egg_nigiri) * egg
        total_score += score
        report_entries.append(ReportEntry(f'Egg Nigiri x {egg}', score))
    if salmon > 0:
        score = get_nigiri_score(salmon_nigiri) * salmon
        total_score += score
        report_entries.append(ReportEntry(f'Salmon Nigiri x {salmon}', score))
    if squid > 0:
        score = get_nigiri_score(squid_nigiri) * squid
        total_score += score
        report_entries.append(ReportEntry(f'Squid Nigiri x {squid}', score))

    tableau = list(np.delete(tableau, indices))
    return tableau, total_score, report_entries
