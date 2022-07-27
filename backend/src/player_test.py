from src.player import make_players


def test_make_players():
    player_names = ["reb", "Cool H"]
    players = make_players(player_names)
    print(players)