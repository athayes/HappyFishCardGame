import random


# Deck factory functions
def basic_deck():
    return make_deck([("Maki", 6), ("Sashimi", 6), ("Salmon", 6)])


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
