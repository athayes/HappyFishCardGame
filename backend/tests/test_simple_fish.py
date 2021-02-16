from simple_fish import make_deck, shuffle_deck, deal_hand, Game
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
    hand, deck = deal_hand(test_deck, 6)
    assert len(hand) == 6
    assert len(deck) == 12
    np.testing.assert_array_equal(test_deck.sort(), (hand + deck).sort())


def test_game_init():
    game = Game(
        ["reb", "Cool H"],
        make_deck([("Maki", 6), ("Sashimi", 6), ("Salmon", 6)]),
        4
    )
    assert game.round == 0
    assert game.players
    assert game.deck


def test_game_start_round():
    game = Game(
        ["reb", "Cool H"],
        make_deck([("Maki", 6), ("Sashimi", 6), ("Salmon", 6)]),
        3
    )
    game.start_round()
    assert game.round == 1
    assert len(game.deck) == 12
    assert len(game.players[0].hand) == 3
