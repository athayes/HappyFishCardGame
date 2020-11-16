import random
import json

class Card:
    face_value = 0
    dessert = False
    
    def __init__(self, face_value=0):
        self.face_value = face_value

    def play(self, hand, tableau):
        tableau += self
        hand.remove(self)

    def __lt__(self, other):
        return self.sort_value < other.sort_value

    def __gt__(self, other):
        return self.sort_value > other.sort_value

    def __str__(self):
        return self.__class__.__name__
        
    def to_json(self):
        data = {}
        data['name'] = 'Maki'
        return data

    @staticmethod
    def score(clazz, tableaus, player_ids, players):
        # Tableaus must be sorted

        for i in range(len(tableaus)):
            j = 0
            while j < len(tableaus[i]) and isinstance(tableaus[i][j], clazz):
                players.get(player_ids[i]).score += clazz.face_value
                j += 1
            if j == len(tableaus[i]):
                tableaus[i] = []
            else:
                tableaus[i] = tableaus[i][j:]
                
    @staticmethod
    def count_dessert(tableaus, player_ids, players):
        # Tableaus must be sorted

        for i in range(len(tableaus)):
            j = 0
            while j < len(tableaus[i]) and isinstance(tableaus[i][j], clazz):
                players.get(player_ids[i]).dessert += 1
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

    def __init__(self, power=1):
        self.power = power

    @staticmethod
    def score(clazz, tableaus, player_ids, players):
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
            players.get(player_ids[i]).score += neg_score

        # Find who came first
        max_score = max(card_cnts)
        max_indices = [index for index, element in enumerate(card_cnts)
                       if max_score == element]
        pos_score = clazz.reward // len(max_indices)
        for i in max_indices:
            players.get(player_ids[i]).score += pos_score
            card_cnts[i] = 0

        # Find who came second
        if clazz.second_reward > 0:
            max_score = max(card_cnts)
            max_indices = [index for index, element in enumerate(card_cnts)
                           if max_score == element]
            pos_score = clazz.second_reward // len(max_indices)
            for i in max_indices:
                players.get(player_ids[i]).score += pos_score


class Threshold_Card(Card):
    reward = 0
    punishment = 0
    min_count = 0
    max_count = 0

    @staticmethod
    def score(clazz, tableaus, player_ids, players):
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
                players.get(player_ids[i]).score += card_cnts[i] // Threshold_Card.min_count
        else:
            pass # how to score negative points?


# Face value score cards
class Nigiri(Card):
    sort_value = 2
    
    def __init__(self):
        super().__init__(random.randint(1, 3))

    @staticmethod
    def score(tableaus, player_ids, players):
        Card().score(Nigiri, tableaus, scores)


class Miso(Card):
    sort_value = 4
    face_value = 3

    @staticmethod
    def score(tableaus, player_ids, players):
        Card().score(Miso, tableaus, player_ids, players)


# No score cards
class Menu(Card):
    sort_value = 5
    face_value = 0

    @staticmethod
    def score(tableaus, player_ids, players):
        Card().score(Menu, tableaus, player_ids, players)


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
    def score(tableaus, player_ids, players):
        Card().score(Spoon, tableaus, player_ids, players)


class Chopsticks(Card):
    face_value = 0
    sort_value = 10

    @staticmethod
    def score(tableaus, player_ids, players):
        Card().score(Chopsticks, tableaus, player_ids, players)


class Tea(Card):
    sort_value = 0


# Combo scoring cards
class Wasabi(Card):
    sort_value = 1

    def __init__(self):
        # score this first so linked nigiri is def not deleted
        super().__init__()
        self.nigiri = None

    @staticmethod
    def score(tableaus, player_ids, players):
        # Tableaus must be sorted

        for i in range(len(tableaus)):
            j = 0
            while j < len(tableaus[i]) and isinstance(tableaus[i][j], Wasabi):
                # The third will be added in the nigiri scoring method
                players.get(player_ids[i]).score += tableaus[i][j].nigiri.face_value * 2
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
        Threshold_Card().score(Tofu, tableaus, player_ids, players)


class Dumpling(Card):
    sort_value = 12
    score_vals = {1: 1, 2: 3, 3: 6, 4: 10, 5: 15}

    @staticmethod
    def score(tableaus, player_ids, players):
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
                    players.get(player_ids[i]).score += val
                    num_dumplings -= k


class Tempura(Threshold_Card):
    sort_value = 13
    reward = 5
    min_count = 2

    @staticmethod
    def score(tableaus, player_ids, players):
        Threshold_Card().score(Tempura, tableaus, player_ids, players)


class Sashimi(Threshold_Card):
    sort_value = 14
    punishment = 0
    reward = 10
    min_count = 3

    @staticmethod
    def score(tableaus, player_ids, players):
        Threshold_Card().score(Sashimi, tableaus, player_ids, players)


class Eel(Threshold_Card):
    sort_value = 15
    reward = 7
    punishment = -3
    min_count = 2

    @staticmethod
    def score(tableaus, player_ids, players):
        Threshold_Card().score(Eel, tableaus, player_ids, players)


class Ice_Cream(Threshold_Card):
    sort_value = 100
    dessert = True
    reward = 12
    punishment = 0

    @staticmethod
    def score(tableaus, player_ids, players):
        Threshold_Card().score(Ice_Cream, tableaus, player_ids, players)


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

    def __init__(self):
        super().__init__(random.randint(1, 3))

    @staticmethod
    def score(tableaus, player_ids, players):
        Army_Card().score(Maki, tableaus, player_ids, players)


class Temaki(Army_Card):
    sort_value = 17
    reward = 4
    punishment = -4

    @staticmethod
    def score(tableaus, player_ids, players):
        Army_Card().score(Temaki, tableaus, player_ids, players)


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

    def __init__(self, card_type):
        super().__init__()
        self.card_type = card_type


class Pudding(Card):
    sort_value = 100
    dessert = True
    reward = 6
    punihsment = -6

    @staticmethod
    def score(tableaus, player_ids, players):
        Army_Card().score(Pudding, tableaus, player_ids, players)


class Deck:
    CARD_DISTRIBUTION = {Nigiri: 12, Maki: 12, Temaki: 12, Uramaki: 12, Tempura: 8,
    Sashimi: 8, Dumpling: 8, Eel: 8, Tofu: 8, Onigiri: 8, Edamame: 8, Miso: 8,
    Chopsticks: 3, Soy: 3, Tea: 3, Menu: 3, Spoon: 3, Special: 3, Takeout: 3,
    Wasabi: 3, Pudding: 15, Ice_Cream: 15, Fruit: 15}    
    cards = []


    def __init__(self, card_types, players):
        self.cards = []
        self.players = players
        for card_type in card_types:
            self.cards.extend([card_type() for i in range(Deck.CARD_DISTRIBUTION.get(card_type))])

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_a_hand(self, num_cards):
        hand = self.cards[0:num_cards]
        self.cards = self.cards[num_cards:-1]
        return hand
        
    def __str__(self):
        return self.cards.__str__()


class Hand:
    def __init__(self, cards, players):
        self.cards = cards
        self.players = players

    def play(self, card, tableau, player):
        self.cards.remove(card)
        self.players.get(player).tableau.add(card)


class Tableau:
    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, key):
        return self.cards[key]

    def add(self, card):
        self.cards.append(card)


class Game:
    SPECIALS = [Miso, Wasabi, Menu, Takeout, Special, Soy, Spoon, Chopsticks, Tea, Edamame]
    ROLLS = [Maki, Temaki, Uramaki]
    APPETIZERS = [Tofu, Dumpling, Tempura, Sashimi, Eel, Onigiri]
    DESSERT = [Pudding, Ice_Cream, Fruit]
    

    CARDS_TO_DEAL = {2: 10, 3: 10, 4: 9, 5: 9, 6: 8, 7: 8, 8: 7}

    def __init__(self, player_names, cards_in_use=[Wasabi, Chopsticks, Dumpling, Tempura, Sashimi], dessert=Pudding):
        self.cards_in_use = cards_in_use
        self.num_players = len(player_names)
        self.round = 0
        self.deck = Deck(cards_in_use, player_names)
        self.dessert = dessert
        self.players = {player: Player(player, self) for player in player_names}
        
    def player_json(self):
        data = {}
        for player_name, player in self.players.items():
            data[player_name] = player.to_json()
        return data
        

    def start_round(self):
        self.round += 1
        self.deck.shuffle()
        
        for player in self.players:
            self.players.get(player).hand = self.deck.deal_a_hand(Game.CARDS_TO_DEAL.get(len(self.players)))


    def score_round(self):
        tableaus = []
        player_ids = [] # dictionaries do not enforce order, so need to hold these static
        for player in players.keys():
            players.get(player).tableau.sort()
            tableaus.add(players.get(player).tableau)
            player_ids.add(player)
        for card_type in self.cards_in_use:  # ensure dessert not counted here
                Card.count_dessert(tableaus, player_ids, self.players)
        card_type.score(card_type, tableaus, player_ids, self.players)

    def score_dessert(self):
        tableaus = []
        player_ids = [] # dictionaries do not enforce order, so need to hold these static
        for player in players.keys():
            players.get(player).tableau.sort()
            tableaus.add(players.get(player).tableau)
            player_ids.add(player)
        self.dessert.score(card_type, tableaus, player_ids, self.players)


class Player():
    def __init__(self, screen_name, game_id):
        self.screen_name = screen_name
        self.game_id = game_id
        self.score = 0
        self.tableau = []
        self.dessert = []
        self.hand = []
        
        
    def to_json(self):
        data = {}
        data['score'] = self.score
        data['tableau'] = self.tableau
        data['dessert'] = self.dessert
        data['hand'] = []
        for c in self.hand:
            data['hand'].extend(c.to_json())
        return data



################ Testing code #####################
if __name__ == "__main__":
    p1 = Player('a', 1)
    p2 = Player('b', 1)
    game = Game([p1, p2])
    chopstick = Chopsticks()
    dum1 = Dumpling()
    dum2 = Dumpling()
    dum3 = Dumpling()
    m1 = Maki()
    m2 = Maki()
    scores = [0, 0]
    #tableaus = [Tableau([dum1]), Tableau([dum2, dum3])]
    # Maki.score(tableaus, scores)
    #Dumpling.score(tableaus, scores)
    print(scores)
