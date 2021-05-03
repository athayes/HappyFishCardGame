import random
from src.cards import egg_nigiri, salmon_nigiri, squid_nigiri, dumpling, \
    tempura, sashimi, pudding, wasabi, maki_1, maki_2


def basic_deck():
    return make_deck([(egg_nigiri, 4), (salmon_nigiri, 4), (squid_nigiri, 4), (maki_1, 4), (maki_2, 4), (maki_1, 3), (tempura, 8),
                      (sashimi, 8), (dumpling, 8), (wasabi, 3), (pudding, 8)])  # todo, dessert distribution each round


def shuffle_deck(deck):
    new_deck = deck.copy()
    random.shuffle(new_deck)
    return new_deck


# A "deck" is just a list of cards (strings), so this can be used to make test hands or tableaus as well
def make_deck(cards):
    deck = []
    for card in cards:
        card_name, card_count = card
        deck.extend([card_name for i in range(card_count)])
    return deck
