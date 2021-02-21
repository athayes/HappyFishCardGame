import numpy as np

from card_names import maki_1, maki_2, maki_3


def score_army_cards(old_players):
    players = old_players
    return players


def score_maki(old_players):
    players = old_players
    players = find_maki_counts(players)
    first_place = 0
    second_place = 0
    for player in players:
        if player.maki_count > first_place:
            first_place = player.maki_count
        elif first_place > player.maki_count > second_place:
            second_place = player.maki_count

    for player in players:
        if player.maki_count == first_place:
            player.score += 6
        if player.maki_count == second_place:
            player.score += 3
        # clean up
        player.maki_count = 0

    return players


def find_maki_counts(old_players):
    players = old_players
    for player_ind, player in enumerate(players):
        maki_count = 0
        card_indices = []
        for card_ind, card in enumerate(player.tableau):
            if is_maki(card):
                maki_count += get_maki_count(card)
                card_indices.append(card_ind)
        player.maki_count = maki_count
        # remove the cards from the player's tableau
        player.tableau = np.delete(player.tableau, card_indices)
    return players


def is_maki(card):
    return card in (maki_1, maki_2, maki_3)


def get_maki_count(maki_card):
    if maki_card == maki_1:
        return 1
    if maki_card == maki_2:
        return 2
    if maki_card == maki_3:
        return 3
    raise Exception("Only accepts Maki cards!")


def count_maki(old_player):
    player = old_player

    return player


def score_players(old_players):
    players = old_players
    for player in players:
        player = score_player(player)
    return players


def score_player(old_player):
    player = old_player
    return player


def score_all(old_players):
    players = old_players
    players = score_army_cards(players)
    players = score_players(players)
    return players
