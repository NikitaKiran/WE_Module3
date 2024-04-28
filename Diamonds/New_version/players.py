from ui import select_card

class Player:
    def __init__(self, suit, displayname):
        self.points = 0
        self.cards = [i for i in range(2, 15)]
        self.suit = suit
        self.displayname = displayname

    def add_points(self, points):
        self.points += points

    def remove_card(self, value):
        self.cards.remove(value)
    
    def get_points(self):
        return self.points
    
    def get_suit(self):
        return self.suit
    
    def get_cards(self):
        return self.cards
    
    def get_displayname(self):
        return self.displayname

class User(Player):
        def __init__(self, displayname, suit):
             super().__init__(suit, displayname)

        def bid(self, diamond_card, opponent_cards, remaining_diamond_cards):
            value = select_card(self)
            self.remove_card(value)
            return value
        
class Computer(Player):
        def __init__(self, displayname, suit, strategy):
            super().__init__(suit, displayname)
            self.strategy = strategy
        
        def bid(self, diamond_card, opponent_cards, remaining_diamond_cards):
            value = self.strategy.get_card_to_bid(diamond_card, self.cards, opponent_cards, remaining_diamond_cards)
            self.remove_card(value)
            return value
        

             
        