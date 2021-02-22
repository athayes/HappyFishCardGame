from typing import List

from src.deck import shuffle_deck
from src.scoring import score_all
from src.player import make_players, find_player, Player


class Game:
    def __init__(self, player_names, deck, hand_size):
        self.deck = deck
        self.players = make_players(player_names)
        self.round = 0
        self.hand_size = hand_size
        self.start_round()

    def start_round(self):
        self.round += 1
        self.deck = shuffle_deck(self.deck)
        players, deck = deal_hands(self.players, self.deck, self.hand_size)
        self.players = players
        self.deck = deck

    def play_card(self, player_name, card_index):
        index, player = find_player(player_name, self.players)
        if player.chosen:
            return player_name + " has already chosen a card"

        card_name = player.hand[card_index]
        if card_name == "Chopsticks":
            # handle chopsticks case here
            # probably return a different json
            return

        player.tableau.append(player.hand.pop(card_index))
        player.chosen = True
        self.players[index] = player

        if not self.check_round_over() and self.all_players_chosen():
            self.players = rotate_hands(self.players)
            for player in self.players:
                player.chosen = False

    def player_json(self):
        data = []
        for player in self.players:
            data.append(player.to_json())
        return data

    def to_json(self):
        return {
            'deck': self.deck,
            "players": self.player_json()
        }

    def check_round_over(self):
        if not self.all_hands_empty():
            return False
        self.score_round()
        if self.round < 2:
            self.start_round()
            return True
        elif self.round == 2:
            # self.score_dessert() TODO
            return True
        return False

    def score_round(self):
        self.players = score_all(self.players)

    def is_player_chosen(self, player):
        index, player = find_player(player, self.players)
        return player.chosen

    def all_players_chosen(self):
        for player in self.players:
            if not player.chosen:
                return False
        return True

    def all_hands_empty(self):
        for player in self.players:
            if not len(player.hand) == 0:
                return False
        return True


# note this function is mutable
def deal_hands(players, deck, hand_size):
    for player in players:
        new_hand, new_deck = deal_hand(deck, hand_size)
        deck = new_deck
        player.hand = new_hand
        player.chosen = False
    return players, deck


def deal_hand(deck, hand_size):
    deck = deck.copy()
    hand = deck[0:hand_size]
    deck = deck[hand_size:]
    return hand, deck

def rotate_hands(players: List[Player]) -> List[Player]:
    old_hands = list(player.hand for player in players)
    hands = old_hands  # assignment gets rid of mutability (player.hand would otherwise be updated)

    for index, hand in enumerate(hands):
        if index == 0:
            players[-1].hand = hand
        else:
            players[index - 1].hand = hand
    return players