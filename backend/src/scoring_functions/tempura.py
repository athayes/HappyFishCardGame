import numpy as np

from src.cards import tempura

def score_tempura(player):
    count = 0
    indices = []
    for index, card in enumerate(player.tableau):
        if card == tempura:
            count += 1
            indices.append(index)
    player.score += get_score_for_tempura_count(count)
    player.tableau = list(np.delete(player.tableau, indices))
    return player

def get_score_for_tempura_count(count):
    return 5 * (count//2)
