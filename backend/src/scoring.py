from src.scoring_functions.army_cards.maki import score_maki


def score_army_cards(old_players):
    players = old_players
    players = score_maki(players)
    return players


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
