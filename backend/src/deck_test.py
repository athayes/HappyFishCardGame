import numpy as np

from src.cards import dumpling
from src.deck import make_deck, shuffle_deck, add_desserts_into_deck, get_dessert_card_count


def test_make_deck():
    deck = make_deck([("Maki", 3), ("Sashimi", 1), ("Salmon", 2)])
    np.testing.assert_array_equal(deck, ["Maki", "Maki", "Maki", "Sashimi", "Salmon", "Salmon"])


def test_shuffle_deck():
    deck = make_deck([("Maki", 6), ("Sashimi", 6), ("Salmon", 6)])
    new_deck = shuffle_deck(deck)
    np.testing.assert_array_equal(deck.sort(), new_deck.sort())


def test_get_dessert_card_count():
    assert get_dessert_card_count(2, 1) == 5
    assert get_dessert_card_count(2, 2) == 3
    assert get_dessert_card_count(2, 3) == 2
    assert get_dessert_card_count(6, 1) == 7
    assert get_dessert_card_count(6, 2) == 5
    assert get_dessert_card_count(6, 3) == 3


def test_add_desserts_into_deck():
    deck = make_deck([("Maki", 5), ("Sashimi", 5), ("Salmon", 5)])
    desserts = make_deck([(dumpling, 10)])
    deck, desserts = add_desserts_into_deck(deck, desserts, 2, 1)
    assert len(desserts) == 5
    assert len(deck) == 20
