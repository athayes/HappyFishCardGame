import random


class Deck:
    def __init__(self, card_types, num_to_deal):
        self.cards = []
        for card_type in card_types:
            self.cards += [card_type() for i in range(num_to_deal)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hand, num_cards):
        hand = self.cards[0:num_cards]
        self.cards = self.cards[num_cards:-1]


class Hand:
    def __init__(self, cards, tableau):
        self.cards = cards
        self.tableau = tableau

    def play(self, card):
        self.cards.remove(card)
        self.tableau.add(card)


class Tableau:
    def __init__(self, cards):
        self.cards = cards

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def add(self, card):
        self.cards.append(card)


class Card:
    face_value = 0
    sort_value = 0
    dessert = False

    def play(self, hand, tableau):
        tableau += self
        hand.remove(self)

    def __lt__(self, other):
        return self.sort_value < other.sort_value

    def __gt__(self, other):
        return self.sort_value > other.sort_value

    def __str__(self):
        return self.__class__.__name__

    @staticmethod
    def score(clazz, tableaus, scores):
        # Tableaus must be sorted

        for i in range(len(tableaus)):
            j = 0
            while j < len(tableaus[i]) and isinstance(tableaus[i][j], clazz):
                scores[i] += clazz.face_value
                j += 1
            if j == len(tableaus[i]):
                tableaus[i] = []
            else:
                tableaus[i] = tableaus[i][j:]


class Army_Card(Card):
    reward = 0
    second_reward = 0
    punishment = 0
    power = 1

    @staticmethod
    def score(clazz, tableaus, scores):
        # Tableaus must be sorted

        card_cnts = [0 for i in range(num_players)]
        for i in range(len(tableaus)):
            j = 0
            while j < len(tableaus[i]) and isinstance(tableaus[i][j], clazz):
                card_cnts[i] += tableaus[i][j].power
                j += 1
            if j == len(tableaus[i]):
                tableaus[i] = []
            else:
                tableaus[i] = tableaus[i][j:]

        # Find who should get negative points (who came last)  
        min_score = min(card_cnts)
        min_indices = [index for index, element in enumerate(card_cnts)
                       if min_score == element]
        neg_score = clazz.punishment // len(min_indices)
        for i in min_indices:
            scores[i] += neg_score

        # Find who came first
        max_score = max(card_cnts)
        max_indices = [index for index, element in enumerate(card_cnts)
                       if max_score == element]
        pos_score = clazz.reward // len(max_indices)
        for i in max_indices:
            scores[i] += pos_score
            card_cnts[i] = 0

        # Find who came second
        if clazz.second_reward > 0:
            max_score = max(card_cnts)
            max_indices = [index for index, element in enumerate(card_cnts)
                           if max_score == element]
            pos_score = clazz.second_reward // len(max_indices)
            for i in max_indices:
                scores[i] += pos_score


class Threshold_Card(Card):
    reward = 0
    punishment = 0
    min_count = 0
    max_count = 0

    @staticmethod
    def score(clazz, tableaus, scores):
        # Tableaus must be sorted

        card_cnts = [0 for i in range(num_players)]
        for i in range(len(tableaus)):
            j = 0
            while j < len(tableaus[i]) and isinstance(tableaus[i][j], clazz):
                card_cnts[i] += 1
                j += 1
            if j == len(tableaus[i]):
                tableaus[i] = []
            else:
                tableaus[i] = tableaus[i][j:]

        if Threshold_Card.min_count > 0:
            for i in range(len(scores)):
                scores[i] += card_cnts[i] // Threshold_Card.min_count
        else:
            pass


# Face value score cards
class Egg(Card):
    face_value = 1
    sort_value = 1

    @staticmethod
    def score(tableaus, scores):
        Card().score(Egg, tableaus, scores)


class Salmon(Card):
    face_value = 2
    sort_value = 2

    @staticmethod
    def score(tableaus, scores):
        Card().score(Salmon, tableaus, scores)


class Squid(Card):
    face_value = 3
    sort_value = 3

    @staticmethod
    def score(tableaus, scores):
        Card().score(Squid, tableaus, scores)


class Miso(Card):
    sort_value = 4
    face_value = 3

    @staticmethod
    def score(tableaus, scores):
        Card().score(Miso, tableaus, scores)


# No score cards
class Menu(Card):
    sort_value = 5
    face_value = 0

    @staticmethod
    def score(tableaus, scores):
        Card().score(Menu, tableaus, scores)


class Takeout(Card):
    sort_value = 6


class Special(Card):
    sort_value = 7


class Soy(Card):
    sort_value = 8


class Spoon(Card):
    sort_value = 9
    face_value = 0

    @staticmethod
    def score(tableaus, scores):
        Card().score(Spoon, tableaus, scores)


class Chopsticks(Card):
    face_value = 0
    sort_value = 10

    @staticmethod
    def score(tableaus, scores):
        Card().score(Chopsticks, tableaus, scores)


class Tea(Card):
    sort_value = -1


# Combo scoring cards
class Wasabi(Card):
    def __init__(self):
        # score this first so linked nigiri is def not deleted
        super().__init__()
        self.nigiri = None

    @staticmethod
    def score(tableaus, scores):
        # Tableaus must be sorted

        for i in range(len(tableaus)):
            j = 0
            while j < len(tableaus[i]) and isinstance(tableaus[i][j], Wasabi):
                # The third will be added in the nigiri scoring method
                scores[i] += tableaus[i][j].nigiri.face_value * 2
                j += 1
            if j == len(tableaus[i]):
                tableaus[i] = []
            else:
                tableaus[i] = tableaus[i][j:]


class Tofu(Threshold_Card):
    sort_value = 11
    max_count = 2
    score_vals = {1: 2, 2: 6}

    @staticmethod
    def score(tableaus, scores):
        Threshold_Card().score(Tofu, tableaus, scores)


class Dumpling(Card):
    sort_value = 12
    score_vals = {1: 1, 2: 3, 3: 6, 4: 10, 5: 15}

    @staticmethod
    def score(tableaus, scores):
        # Tableaus must be sorted

        for i in range(len(tableaus)):
            j = 0
            num_dumplings = 0
            while j < len(tableaus[i]) and isinstance(tableaus[i][j], Dumpling):
                num_dumplings += 1
                j += 1
            if j == len(tableaus[i]):
                tableaus[i] = []
            else:
                tableaus[i] = tableaus[i][j:]

            # Add the scores
            for k in range(5, 0, -1):
                val = Dumpling.score_vals[k] * (num_dumplings // k)
                if val > 0:
                    scores[i] += val
                    num_dumplings -= k


class Tempura(Threshold_Card):
    sort_value = 13
    reward = 5
    min_count = 2

    @staticmethod
    def score(tableaus, scores):
        Threshold_Card().score(Tempura, tableaus, scores)


class Sashimi(Threshold_Card):
    sort_value = 14
    punishment = 0
    reward = 10
    min_count = 3

    @staticmethod
    def score(tableaus, scores):
        Threshold_Card().score(Sashimi, tableaus, scores)


class Eel(Threshold_Card):
    sort_value = 15
    reward = 7
    punishment = -3
    min_count = 2

    @staticmethod
    def score(tableaus, scores):
        Threshold_Card().score(Eel, tableaus, scores)


class Ice_Cream(Threshold_Card):
    sort_value = 100
    dessert = True
    reward = 12
    punishment = 0

    @staticmethod
    def score(tableaus, scores):
        Threshold_Card().score(Ice_Cream, tableaus, scores)


class Fruit(Card):
    sort_value = 100
    dessert = True
    score_vals = {0: -2, 1: 0, 2: 1, 3: 3, 4: 6, 5: 10}

    def __init__(self, type):
        super().__init__()
        self.type = type


# Other player-dependent cards
class Maki(Army_Card):
    sort_value = 16
    reward = 6
    second_reward = 3

    def __init__(self, power):
        super().__init__()
        self.power = power

    @staticmethod
    def score(tableaus, scores):
        Army_Card().score(Maki, tableaus, scores)


class Temaki(Army_Card):
    sort_value = 17
    reward = 4
    punishment = -4

    @staticmethod
    def score(tableaus, scores):
        Army_Card().score(Temaki, tableaus, scores)


class Uramaki(Card):
    sort_value = 20

    def __init__(self, power):
        super().__init__()
        self.power = power


class Edamame(Card):
    sort_value = 18


class Onigiri(Card):
    score_vals = {1: 1, 2: 4, 3: 9, 4: 16}
    sort_value = 19

    def __init__(self, type):
        super().__init__()
        self.type = type


class Pudding(Card):
    sort_value = 100
    dessert = True
    reward = 6
    punihsment = -6

    @staticmethod
    def score(tableaus, scores):
        Army_Card().score(Pudding, tableaus, scores)


class Game:
    SPECIALS = [Miso, Wasabi, Menu, Takeout, Special, Soy, Spoon, Chopsticks, Tea, Edamame]
    ROLLS = [Maki, Temaki, Uramaki]
    APPETIZERS = [Tofu, Dumpling, Tempura, Sashimi, Eel, Onigiri]
    DESSERT = [Pudding, Ice_Cream, Fruit]

    CARDS_TO_DEAL = {2: 10, 3: 10, 4: 9, 5: 9, 6: 8, 7: 8, 8: 7}

    def __init__(self, players, cards_in_use=[Wasabi, Chopsticks, Dumpling, Tempura, Sashimi, Ice_Cream]):
        self.cards_in_use = cards_in_use
        self.players = players
        self.round = 0
        self.deck = Deck(cards_in_use, Game.CARDS_TO_DEAL[len(players)])
        self.tableaus = [Tableau([]) for i in range(len(players))]
        self.hands = [Hand([], self.tableaus[i]) for i in range(len(players))]
        self.scores = [0 for i in range(len(players))]

    def start_round(self):
        self.round += 1
        self.deck.shuffle()
        # How to keep pudding?

        for hand in self.hands:
            self.deck.deal(hand, Game.CARDS_TO_DEAL.get(self.num_players))

    def score_round(self):
        for tableau in tableaus:
            tableau.sort()
        for card_type in self.cards_in_use:  # ensure dessert not counted here
            card_type.score(card_type, tableaus, scores)

    def score_dessert(self):
        pass


class Player():
    def __init__(self, screen_name, game_id):
        self.screen_name = screen_name
        self.game_id = game_id



################ Testing code #####################
if __name__ == "__main__":
    chopstick = Chopsticks()
    dum1 = Dumpling()
    dum2 = Dumpling()
    dum3 = Dumpling()
    m1 = Maki(2)
    m2 = Maki(3)
    scores = [0, 0]
    num_players = 7
    tableaus = [Tableau([dum1]), Tableau([dum2, dum3])]
    # Maki.score(tableaus, scores)
    Dumpling.score(tableaus, scores)
    print(scores)
