from copy import deepcopy
import numpy as np
from src.cards import chopsticks

def handle_chopsticks(player, card_1_index, card_2_index):
    copied_hand = deepcopy(player.hand)
    chopsticks_index = player.tableau.index(chopsticks)
    chosen_cards = [copied_hand[card_1_index], copied_hand[card_2_index]]
    player.hand = list(np.delete(player.hand, [card_1_index, card_2_index]))
    player.tableau = list(np.delete(player.tableau, [chopsticks_index]))
    player.tableau.extend(chosen_cards)
    player.hand.append(chopsticks)
    return player