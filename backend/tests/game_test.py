from src.cards import egg_nigiri
from src.deck import make_deck
from src.game import deal_hand, Game, rotate_hands
from src.player import make_players, find_player
import numpy as np


def test_deal_hand():
    test_deck = make_deck([("Maki", 6), ("Sashimi", 6), ("Salmon", 6)])
    hand, deck = deal_hand(test_deck, 6)
    assert len(hand) == 6
    assert len(deck) == 12
    np.testing.assert_array_equal(test_deck.sort(), (hand + deck).sort())

def test_rotate_hands():
    players = make_players(["P_Zero", "P_One", "P_Two", "P_Three"])
    players[0].hand = make_deck([("H_Zero", 3)])
    players[1].hand = make_deck([("H_One", 3)])
    players[2].hand = make_deck([("H_Two", 3)])
    players[3].hand = make_deck([("H_Three", 3)])
    players = rotate_hands(players)
    np.testing.assert_array_equal(players[0].hand, make_deck([("H_One", 3)]))
    np.testing.assert_array_equal(players[1].hand, make_deck([("H_Two", 3)]))
    np.testing.assert_array_equal(players[2].hand, make_deck([("H_Three", 3)]))
    np.testing.assert_array_equal(players[3].hand, make_deck([("H_Zero", 3)]))


# Just to confirm numpy.delete works as expected
def test_np_delete():
    hand = ["0", "1", "2", "3", "4", "5"]
    new_hand = list(np.delete(hand, [0, 2, 4]))
    np.testing.assert_array_equal(new_hand, ["1", "3", "5"])


# Game class tests
def test_to_json():
    game = Game(
        ["reb", "Cool H"],
        make_deck([("Maki", 6), ("Sashimi", 6), ("Salmon", 6)]),
        3
    )
    json = game.to_json()
    print(json)


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
    game.play_card("Cool H", 0)

    reb_index, reb = find_player("reb", game.players)
    coolh_index, coolh = find_player("Cool H", game.players)
    assert len(reb.hand) == 2
    assert len(reb.tableau) == 1
    assert not coolh.chosen
    assert not reb.chosen

def test_score_round():
    game = Game(
        ["reb", "Cool H"],
        make_deck([("Maki", 6), ("Sashimi", 6), ("Salmon", 6)]),
        3
    )
    game.players[0].tableau = make_deck([(egg_nigiri, 3)])
    game.players[1].tableau = make_deck([(egg_nigiri, 3)])
    game.score_round()

    reb_index, reb = find_player("reb", game.players)
    coolh_index, coolh = find_player("Cool H", game.players)
    print(game.to_json())
    assert reb.score == 3
    assert coolh.score == 3