from copy import deepcopy
import numpy as np
from src.cards import chopsticks

def handle_chopsticks(player, card_1_index):
    copied_hand = deepcopy(player.hand)
    chopsticks_index = player.tableau.index(chopsticks)
    chosen_card = copied_hand[card_1_index]
    player.hand = list(np.delete(player.hand, [card_1_index]))
    player.tableau = list(np.delete(player.tableau, [chopsticks_index]))
    player.tableau.append(chosen_card)
    player.hand.append(chopsticks)
    return player

def remove_chopsticks(player):
    indices = []
    for index, card in enumerate(player.tableau):
        if card == chopsticks:
            indices.append(index)
    player.tableau = list(np.delete(player.tableau, indices))
    return player
