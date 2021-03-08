import numpy as np

from src.cards import sashimi

def score_sashimi(player):
    count = 0
    indices = []
    for index, card in enumerate(player.tableau):
        if card == sashimi:
            count += 1
            indices.append(index)
    player.score += get_score_for_sashimi_count(count)
    player.tableau = list(np.delete(player.tableau, indices))
    return player

def get_score_for_sashimi_count(count):
    return 10 * (count//3)
