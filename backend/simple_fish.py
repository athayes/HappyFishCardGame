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


# players is an array now, not a dict
def make_players(player_names):
    players = []
    for player_name in player_names:
        players.append(Player(player_name))
    return players


def find_player(player_name, players):
    for index, player in enumerate(players):
        if player.player_name == player_name:
            return index, player
    raise ValueError("player not found in list")


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

    # Play method is now in the Game class, so we always have access to the whole state
    # Methods to find players and cards in players hands are pure functions
    def play_card(self, player_name, card_index):
        index, player = find_player(player_name, self.players)

        card_name = player.hand[card_index]
        if card_name == "Chopsticks":
            # handle chopsticks case here
            # probably return a different json
            return

        player.tableau.append(player.hand.pop(card_index))
        player.chosen = True
        self.players[index] = player

    # def to_json(self):
    #     data = {}
    #     data['players'] = self.players
    #     # data['dessert'] = self.dessert
    #     # data['hand'] = self.hand.to_json()
    #     return data


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
