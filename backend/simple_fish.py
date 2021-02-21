import random
from copy import deepcopy


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


def rotate_hands(players):
    old_hands = list(player.hand for player in players)
    hands = old_hands  # assignment gets rid of mutability (player.hand would otherwise be updated)

    for index, hand in enumerate(hands):
        if index == 0:
            players[-1].hand = hand
        else:
            players[index - 1].hand = hand
    return players


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
        # self.score_round() TODO
        if self.round < 2:
            self.start_round()
            return True
        elif self.round == 2:
            # self.score_dessert() TODO
            return True
        return False

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


class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0
        self.tableau = []
        self.dessert = []
        self.hand = []
        self.chosen = False

    def to_json(self):
        return {
            'player_name': self.player_name,
            'score': self.score,
            'tableau': self.tableau,
            'dessert': self.dessert,
            'hand': self.hand
        }

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
