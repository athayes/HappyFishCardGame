from simple_fish import make_deck, shuffle_deck, deal_hand
import numpy as np


def test_make_deck():
    cards = [("Maki", 3), ("Sashimi", 1), ("Salmon", 2)]
    deck = make_deck(cards)
    np.testing.assert_array_equal(deck, ["Maki", "Maki", "Maki", "Sashimi", "Salmon", "Salmon"])


def test_shuffle_deck():
    deck = make_deck([("Maki", 6), ("Sashimi", 6), ("Salmon", 6)])
    new_deck = shuffle_deck(deck)
    np.testing.assert_array_equal(deck.sort(), new_deck.sort())

def test_deal_hand():
    test_deck = make_deck([("Maki", 6), ("Sashimi", 6), ("Salmon", 6)])
    result = deal_hand(test_deck, 6)
    hand = result["hand"]
    deck = result["deck"]
    assert len(hand) == 6
    assert len(deck) == 12
    # np.testing.assert_array_equal(test_deck, (hand.extend(deck)).sort)