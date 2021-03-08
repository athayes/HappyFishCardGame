from src.scoring_functions.army_cards.maki import score_maki
from src.scoring_functions.dumplings import score_dumplings
from src.scoring_functions.sashimi import score_sashimi
from src.scoring_functions.tempura import score_tempura
from src.scoring_functions.wasabi_and_nigiri import score_wasabi_and_nigiri


def score_all(players):
    players = score_army_cards(players)
    players = score_players(players)
    return players


def score_army_cards(old_players):
    players = old_players
    players = score_maki(players)
    return players


def score_players(old_players):
    players = []
    for player in old_players:
        players.append(score_player(player))
    return players


def score_dessert(players):
    return players

def score_player(player):
    player = score_dumplings(player)
    player = score_tempura(player)
    player = score_sashimi(player)
    player = score_wasabi_and_nigiri(player)
    return player
