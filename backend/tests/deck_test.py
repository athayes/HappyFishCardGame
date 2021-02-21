import numpy as np

from src.deck import make_deck, shuffle_deck


def test_make_deck():
    cards = [("Maki", 3), ("Sashimi", 1), ("Salmon", 2)]
    deck = make_deck(cards)
    np.testing.assert_array_equal(deck, ["Maki", "Maki", "Maki", "Sashimi", "Salmon", "Salmon"])


def test_shuffle_deck():
    deck = make_deck([("Maki", 6), ("Sashimi", 6), ("Salmon", 6)])
    new_deck = shuffle_deck(deck)
    np.testing.assert_array_equal(deck.sort(), new_deck.sort())