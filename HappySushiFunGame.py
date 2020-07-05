import random

class Deck:
    def __init__(self, card_types, num_to_deal):
    
        self.cards = [];
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
        self.tableau.append(card)

class Tableau:
    def __init__(self, cards):
        self.cards = cards


class Card:
    face_value = 0
    sort_value = 0
    dessert = False

    def play(self):
        pass

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
                scores[i] += tableaus[i][j].face_value
                j += 1
            if j == len(tableaus[i]):
                tableaus[i] = []
            else:
                tableaus[i] = tableaus[i][j:]



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
    face_value = 3
    sort_value = 4

# No score cards       
class Menu(Card):
    sort_value = 5

class Takeout(Card):
    sort_value = 6

class Special(Card):
    sort_value = 7

class Soy(Card):
    sort_value = 8

class Spoon(Card):
    sort_value = 9

class Chopsticks(Card):
    sort_value = 10

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

class Tofu(Card):
    face_value = 2
    sort_value = 11

class Dumpling(Card):
    sort_value = 12

class Tempura(Card):
    sort_value = 13

class Sashimi(Card):
    sort_value = 14
        
    def score(self):
        pass

class Eel(Card):
    face_value = -3
    sort_value = 15

class Ice_Cream(Card):
    sort_value = 100
    dessert = True
        
class Fruit(Card):
    sort_value = 100
    dessert = True

    def __init__(self, type):
        super().__init__()
        self.type = type

# Other player-dependent cards
class Maki(Card):
    sort_value = 16
    reward = 3
    punishment = -3

    def __init__(self, power):
        super().__init__()
        self.power = power

class Temaki(Card):
    sort_value = 17
    reward = 4
    punishment = -4
        
class Uramaki(Card):
    sort_value = 20

    def __init__(self, power):
        super().__init__()
        self.power = power

class Edamame(Card):
    sort_value = 18


class Onigiri(Card):
    face_value = 1
    sort_value = 19

    def __init__(self, type):
        super().__init__()
        self.type = type

class Pudding(Card):
    sort_value = 100
    dessert = True
    reward = 6
    punihsment = -6

class Game:
    SPECIALS = [Miso, Wasabi, Menu, Takeout, Special, Soy, Spoon, Chopsticks, Tea, Edamame]
    ROLLS = [Maki, Temaki, Uramaki]
    APPETIZERS = [Tofu, Dumpling, Tempura, Sashimi, Eel, Onigiri]
    DESSERT = [Pudding, Ice_Cream, Fruit]

    INTERACTION_CARDS = [Maki, Temaki, Miso, Pudding]
    CARDS_TO_DEAL = {2:10, 3:10, 4:9, 5:9, 6:8, 7:8, 8:7}
   
    def __init__(self, num_players, tableau_interaction, cards_in_use):
        self.cards_in_use = cards_in_use
        self.rnd = 0
        self.deck = Deck(cards_in_use, CARDS_TO_DEAL[num_players])
        self.tableaus = [Tableau() for i in range(num_players)]
        self.hands = [Hand([], self.tableaus[i]) for i in range(num_players)]
        self.scores = [0 for i in range(num_players)]
        self.num_players = num_players

    def start_round(self):
        self.round += 1
        self.deck.shuffle()
        # How to keep pudding?
        
        for hand in self.hands:
            self.deck.deal(hand, CARDS_TO_DEAL.get(self.num_players))

    def score_round(self):
        for tableau in tableaus:
            tableau.sort()
        for card_type in cards_in_use:
            card_type.score(card_type, tableaus, scores)