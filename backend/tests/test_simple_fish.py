from simple_fish import make_deck, shuffle_deck, deal_hand, Game, make_players, find_player
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


def test_make_players():
    player_names = ["reb", "Cool H"]
    players = make_players(player_names)
    print(players)


def test_game_init_start_round():
    game = Game(
        ["reb", "Cool H"],
        make_deck([("Maki", 6), ("Sashimi", 6), ("Salmon", 6)]),
        3
    )
    assert game.round == 1
    assert len(game.deck) == 12
    assert len(game.players) == 2
    assert len(game.players[0].hand) == 3


def test_game_play_card():
    game = Game(
        ["reb", "Cool H"],
        make_deck([("Maki", 6), ("Sashimi", 6), ("Salmon", 6)]),
        3
    )
    game.play_card("reb", 0)
    index, reb = find_player("reb", game.players)
    assert len(reb.hand) == 2
    assert len(reb.tableau) == 1

