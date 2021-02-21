import numpy as np

from src.cards import is_maki, get_maki_number


def score_army_cards(old_players):
    players = old_players
    return players


def score_maki(old_players):
    players = old_players
    players = find_maki_counts(players)
    counts = []
    for player in players:
        counts.append(player.maki_count)
    unique_counts = np.unique(counts)
    unique_counts_ordered = list(reversed(unique_counts))

    for player in players:
        if player.maki_count == unique_counts_ordered[0]:
            player.score += 6
        if player.maki_count == unique_counts_ordered[1]:
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
                maki_count += get_maki_number(card)
                card_indices.append(card_ind)
        player.maki_count = maki_count
        # remove the cards from the player's tableau
        player.tableau = np.delete(player.tableau, card_indices)
    return players


def count_maki(old_player):
    player = old_player

    return player


# TODO
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
