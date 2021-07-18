import numpy as np

from src.cards import chopsticks


def remove_chopsticks(player):
    indices = []
    for index, card in enumerate(player.tableau):
        if card == chopsticks:
            indices.append(index)
    player.tableau = list(np.delete(player.tableau, indices))
    return player
