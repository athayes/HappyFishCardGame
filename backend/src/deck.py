import random
from src.cards import egg_nigiri, salmon_nigiri, squid_nigiri, dumpling, tempura, sashimi, chopsticks


# Deck factory functions
def basic_deck():
    return make_deck([(egg_nigiri, 15), (salmon_nigiri, 15), (squid_nigiri, 15), (dumpling, 15), (tempura, 15), (sashimi, 15)])

def chopsticks_deck():
    return make_deck([(egg_nigiri, 15), (chopsticks, 15)])


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
