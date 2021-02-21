import random


# Deck factory functions
from src.cards import egg_nigiri, salmon_nigiri, squid_nigiri


def basic_deck():
    return make_deck([(egg_nigiri, 6), (salmon_nigiri, 6), (squid_nigiri, 6)])


def shuffle_deck(deck):
    new_deck = deck.copy()
    random.shuffle(new_deck)
    return new_deck


# A "deck" is just a list of cards, so this can be used to make test hands or tableaus as well
def make_deck(cards):
    deck = []
    for card in cards:
        card_name, card_count = card
        deck.extend([card_name for i in range(card_count)])
    return deck
