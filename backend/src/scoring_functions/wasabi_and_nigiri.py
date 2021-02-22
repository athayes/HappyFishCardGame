import numpy as np

from src.cards import wasabi, is_nigiri, get_nigiri_score


def score_wasabi_and_nigiri(arg_player):
    player = arg_player
    tableau, wasabi_score = score_wasabi(player.tableau)
    tableau, nigiri_score = score_nigiri(tableau)
    player.tableau = tableau
    player.score += (wasabi_score + nigiri_score)
    return player


def score_wasabi(arg_tableau):
    tableau = arg_tableau
    indices = []
    score = 0
    for index, card in enumerate(tableau):
        if card == wasabi:
            # find next nigiri
            for other_index, other_card in enumerate(tableau[index:]):
                if is_nigiri(other_card):
                    score += get_nigiri_score(other_card) * 3
                    indices.append(other_index)
                    # mark the card as "played" so it can't be picked up by next wasabi
                    tableau[other_index] = "played_nigiri"
                    break  # leave the loop, found our match
            wasabi_index = index
            indices.append(wasabi_index)

    tableau = list(np.delete(tableau, indices))
    return tableau, score

def score_nigiri(arg_tableau):
    tableau = arg_tableau
    indices = []
    score = 0
    for index, card in enumerate(tableau):
        if is_nigiri(card):
            score += get_nigiri_score(card)
            indices.append(index)

    tableau = list(np.delete(tableau, indices))
    return tableau, score