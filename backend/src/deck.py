# Deck factory functions
def basic_deck():
    return make_card_list([("Maki", 6), ("Sashimi", 6), ("Salmon", 6)])


def make_card_list(cards):
    deck = []
    for card in cards:
        card_name, card_count = card
        deck.extend([card_name for i in range(card_count)])
    return deck