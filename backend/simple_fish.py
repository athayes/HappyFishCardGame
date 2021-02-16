import random
from collections import OrderedDict


# cards is an array of tuples (pairs)
def make_deck(cards):
    deck = []
    for card in cards:
        card_name, card_count = card
        deck.extend([card_name for i in range(card_count)])
    return deck


def shuffle_deck(deck):
    new_deck = deck.copy()
    random.shuffle(new_deck)
    return new_deck


def deal_hand(deck, hand_size):
    new_deck = deck.copy()
    hand = new_deck[0:hand_size]
    new_deck = deck[hand_size:]
    return hand, new_deck


# Python doesn't allow the creation of a dictionary with a variable as a key
# (it can, but it's too complicated to justify the effort)
# So lets use an array
# Anthony will update the frontend to match this
def make_players(player_names):
    players = []
    for player_name in player_names:
        players.append(Player(player_name))
    return players


class Game:
    def __init__(self, player_names, deck, hand_size):
        self.deck = deck
        self.players = make_players(player_names)
        self.round = 0
        self.hand_size = hand_size

    def start_round(self):
        self.round += 1
        self.deck = shuffle_deck(self.deck)
        players = []
        for player in self.players:
            hand, deck = deal_hand(self.deck, self.hand_size)
            self.deck = deck
            player.chosen = False
            player.hand = hand
            players.append(player)
        self.players = players

    # def rotate_hands(self):
    #     new_players = []
    #     hands = filter((lambda player: player.hands), self.players)
    #
    #     for index, value in hands:
    #         if index !== 0:
    #             self.players


#     def check_round_over(self):
#         start_new_round = True
#         for player in self.players:
#             start_new_round = start_new_round and self.players.get(player).hand_empty
#         print(start_new_round)
#         if start_new_round:
#             self.score_round()
#             if start_new_round and self.round < 2:
#                 self.start_round()
#                 return True
#             elif start_new_round and self.round == 2:
#                 self.score_dessert()
#                 return True
#             return False
#
#     def check_all_players_chosen(self):
#         all_chosen = True
#         for player in self.players:
#             all_chosen = all_chosen and self.players.get(player).chosen
#         return all_chosen
#
#


class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0
        self.tableau = []
        self.dessert = []
        self.hand = []
        self.chosen = False

    # def play(self, index):
    #     self.tableau.add(self.hand.cards.pop(index))
    #     self.chosen = True
    #
    # def to_json(self):
    #     data = {}
    #     data['score'] = self.score
    #     data['tableau'] = self.tableau.to_json()
    #     data['dessert'] = self.dessert
    #     data['hand'] = self.hand.to_json()
    #     return data

################ Testing code #####################
# if __name__ == "__main__":
#     p1 = Player('a', 1)
#     p2 = Player('b', 1)
#     game = Game([p1, p2])
#     chopstick = Chopsticks()
#     dum1 = Dumpling()
#     dum2 = Dumpling()
#     dum3 = Dumpling()
#     m1 = Maki()
#     m2 = Maki()
#     scores = [0, 0]
#     # tableaus = [Tableau([dum1]), Tableau([dum2, dum3])]
#     # Maki.score(tableaus, scores)
#     # Dumpling.score(tableaus, scores)
#     print(scores)
