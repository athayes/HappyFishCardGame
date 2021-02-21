def basic_deck():
    return make_deck([("Maki", 6), ("Sashimi", 6), ("Salmon", 6)])


def make_deck(cards):
    deck = []
    for card in cards:
        card_name, card_count = card
        deck.extend([card_name for i in range(card_count)])
    return deck

