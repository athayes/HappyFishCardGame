import random
from src.cards import egg_nigiri, salmon_nigiri, squid_nigiri, dumpling, \
    tempura, sashimi, pudding, wasabi, maki_1, maki_2, maki_3, chopsticks


def basic_deck():
    cards = [
        {'type': 'Nigiri', 'name': 'Nigiri'},
        {'type': 'Rolls', 'name': 'Maki'},
        {'type': 'Appetizer', 'name': tempura},
        {'type': 'Appetizer', 'name': sashimi},
        {'type': 'Appetizer', 'name': dumpling},
        {'type': 'Special', 'name': chopsticks},
        {'type': 'Special', 'name': wasabi},
        {'type': 'Dessert', 'name': pudding},
    ]
    deck, desserts = custom_deck(cards)
    return deck, desserts


def custom_deck(cards):
    deck = []
    dessert = []
    for card in cards:
        ctype = card['type']
        name = card['name']

        if ctype == 'Nigiri':
            deck.append((egg_nigiri, 4))
            deck.append((salmon_nigiri, 4))
            deck.append((squid_nigiri, 4))
        if ctype == "Rolls":
            if name == "Maki":
                deck.append((maki_1, 4))
                deck.append((maki_2, 4))
                deck.append((maki_3, 4))
            else:
                deck.append((name, 12))
        if ctype == "Special":
            deck.append((name, 3))
        if ctype == "Appetizer":
            deck.append((name, 8))
        if ctype == "Dessert":
            dessert.append((name, 8))
    return make_deck(deck), make_deck(dessert)


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
    desserts = desserts[card_count - 1:-1]

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
