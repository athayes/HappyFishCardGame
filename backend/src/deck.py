import random
from src.cards import egg_nigiri, salmon_nigiri, squid_nigiri, dumpling, \
    tempura, sashimi, pudding, wasabi, maki_1, maki_2


def basic_deck():
    deck = make_deck(
        [(egg_nigiri, 4), (salmon_nigiri, 4), (squid_nigiri, 4), (maki_1, 4), (maki_2, 4), (maki_1, 3), (tempura, 8),
         (sashimi, 8), (dumpling, 8), (wasabi, 3)])
    return deck


def basic_desserts():
    return make_deck([(pudding, 8)])


def shuffle_deck(deck):
    new_deck = deck.copy()
    random.shuffle(new_deck)
    return new_deck


def add_desserts_into_deck(deck, desserts, num_players, round):
    desserts = shuffle_deck(desserts)
    card_count = get_dessert_card_count(num_players, round)

    if card_count > len(desserts):
        card_count = len(desserts)

    deck.extend(desserts[0:card_count])
    desserts = desserts[card_count-1:-1]

    return deck, desserts


def get_dessert_card_count(num_players, round):
    if num_players <= 5:
        if round == 1:
            return 5
        if round == 2:
            return 3
        if round == 3:
            return 2

    if round == 1:
        return 7
    if round == 2:
        return 5
    if round == 3:
        return 3


# A "deck" is just a list of cards (strings), so this can be used to make test hands or tableaus as well
def make_deck(cards):
    deck = []
    for card in cards:
        card_name, card_count = card
        deck.extend([card_name for i in range(card_count)])
    return deck
