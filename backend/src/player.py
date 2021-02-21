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