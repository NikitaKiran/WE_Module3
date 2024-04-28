from ui import select_card

class Player:
    def __init__(self, suit):
        self.points = 0
        self.cards = [i for i in range(2, 15)]
        self.suit = suit

    def add_points(self, points):
        self.points += points

    def remove_card(self, value):
        self.cards.remove(value)
    
    def get_points(self):
        return self.points
    
    def get_suit(self):
        return self.suit

class User(Player):
        def __init__(self, suit):
             super().__init__(suit)

        def bid(self, diamond_card, opponent_cards, remaining_diamond_cards):
            value = select_card(self)
            return super.bid(self, value)
        
class Computer(Player):
        def __init__(self, suit, strategy):
            super().__init__(suit)
            self.strategy = strategy
        
        def bid(self, diamond_card, opponent_cards, remaining_diamond_cards):
            value = self.strategy.get_card_to_bid(diamond_card, self.cards, opponent_cards, remaining_diamond_cards)
            return super.bid(self, value)
        

             
        