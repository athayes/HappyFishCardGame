from src.player import ScoreReport
from src.scoring_functions.army_cards.maki import score_maki
from src.scoring_functions.dessert.ice_cream import score_ice_cream
from src.scoring_functions.dessert.pudding import score_pudding
from src.scoring_functions.dumplings import score_dumplings
from src.scoring_functions.eel import score_eel
from src.scoring_functions.no_score_cards.chopsticks import remove_chopsticks
from src.scoring_functions.sashimi import score_sashimi
from src.scoring_functions.tea import score_tea
from src.scoring_functions.tempura import score_tempura
from src.scoring_functions.wasabi_and_nigiri import score_wasabi_and_nigiri
from src.scoring_functions.army_cards.temaki import score_temaki
from src.scoring_functions.army_cards.edamame import score_edamame


def score_all(players):
    players = score_players(players)
    players = score_army_cards(players)
    return players


def score_army_cards(old_players):
    players = old_players
    players = score_maki(players)
    players = score_temaki(players)
    players = score_edamame(players)
    return players


def score_players(old_players):
    players = []
    for player in old_players:
        players.append(score_player(player))
    return players


def score_dessert(players):
    players = score_pudding(players)
    players = score_ice_cream(players)
    return players


def score_player(player):
    player.score_report = ScoreReport()
    player.score_report.score_round_start = player.score
    player.score_report.tableau = player.tableau
    player.score_report.dessert = player.dessert
    player = score_tea(player)
    player = score_dumplings(player)
    player = score_tempura(player)
    player = score_sashimi(player)
    player = score_wasabi_and_nigiri(player)
    player = score_eel(player)
    player = remove_chopsticks(player)
    player.score_report.score_round_end = player.score
    return player
