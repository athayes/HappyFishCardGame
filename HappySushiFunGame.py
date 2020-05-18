import random

class Game:
    SPECIALS = ["Miso", "Wasabi", "Menu", "Takeout", "Special", "Soy", "Spoon", "Chopsticks", "Tea", "Edamame"]
    ROLLS = ["Maki", "Temaki", "Uramaki"]
    APPETIZERS = ["Tofu", "Dumpling", "Tempura", "Sashimi", "Eel", "Onigiri"]
    DESSERT = ["Pudding", "Ice Cream", "Fruit"]

    INTERACTION_CARDS = ["Maki", "Temaki", "Miso", "Pudding"]
    CARDS_TO_DEAL = {2:10, 3:10, 4:9, 5:9, 6:8, 7:8, 8:7}
   
    def __init__(self, deck, num_players, tableau_interaction, num_players)
       self.round = 0
       self.deck = deck
       self.tableaus = [Tableau() for i in range(num_players)]
       self.hands = [Hand([], self.tableaus[i]) for i in range(num_players)]
       self.scores = [0 for i in range(num_players)]
       self.num_players = num_players
       self.board_interaction = tableau_interaction # if using maki, temaki, miso, or pudding

    def start_round(self):
        self.round += 1
        self.deck.shuffle()
        # How to keep pudding?
        
        for hand in self.hands:
            self.deck.deal(hand, CARDS_TO_DEAL.get(self.num_players))

    def score_round(self):
        
        


class Deck:
    def __init__(self, cards):
        self.cards = cards

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
        self.tableu.append(card)

class Tableau:
    def __init__(self, cards):
        self.cards = cards


class Card:
    def __init__(self, face_value):
        self.face_value = face_value
        
    def play(self):
        pass
    
    def score(self):
        return self.face_value
        
    def __str__(self):
        return self.__class__.__name__


# Face value score cards
class Egg(Card):
    def __init__(self):
        Super(self, 1)

class Salmon(Card):
    def __init__(self):
        Super(self, 2)

class Squid(Card):
    def __init__(self):
        Super(self, 3)
        
class Miso(Card):
    def __init__(self):
        Super(self, 3)

# No score cards       
class Menu(Card):
    def __init__():
        Super(self, 0)

class Takeout(Card):
    def __init__(self):
        Super(self, 0)

class Special(Card):
    def __init__(self):
        Super(self, 0)

class Soy(Card):
    def __init__(self):
        Super(self, 0)

class Spoon(Card):
    def __init__(self):
        Super(self, 0)

class Chopsticks(Card):
    def __init__(self):
        Super(self, 0)

class Tea(Card):
    def __init__(self):
        Super(self, 1)

# Combo scoring cards
class Wasabi(Card):
    def __init__(self):
        Super(self, 0)
        self.nigiri = none
        
    def score(self);
        if self.nigiri == none:
            Super.score()
        else:
            return self.nigiri.face_value * 2

class Tofu(Card):
    def __init__(self):
        Super(self, 2)

class Dumpling(Card):
    def __init__(self):
        Super(self, 1)

class Tempura(Card):
    def __init__(self):
        Super(self, 0)

class Sashimi(Card):
    def __init__(self):
        Super(self, 0)
        
    def score(self):

class Eel(Card):
    def __init__(self):
        Super(self, -3)

class Ice_Cream(Card):
    def __init__(self):
        Super(self, 0)
        
class Fruit(Card):
    def __init__(self, type):
        Super(self, 0)
        self.type = type

# Other player-dependent cards
class Maki(Card):
    def __init__(self, power):
        Super(self, 0)
        self.power = power
        self.reward = 3
        self.punishment = -3

class Temaki(Card):
    def __init__(self):
        Super(self, 0)
        self.reward = 4
        self.punishment = -4
        
class Uramaki(Card):
    def __init__(self, power):
        Super(self, 0)
        self.power = power

class Edamame(Card):
    def __init__(self):
        Super(self, 0)

class Onigiri(Card):
    def __init__(self, type):
        Super(self, 1)
        self.type = type

class Pudding(Card):
    def __init__(self):
        Super(self, 0)
        self.reward = 6
        self.punishment = -6