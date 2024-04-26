from ui import select_card
import random

class Player:
    def __init__(self, suit):
        self.points = 0
        self.cards = [i for i in range(2, 15)]
        self.suit = suit

    def add_points(self, points):
        self.points += points


class User(Player):
        def __init__(self, suit):
             super().__init__(suit)

        def bid(self):
            bid = select_card(self)
            self.cards.remove(bid)
            return bid
        
class Computer(Player):
        def __init__(self, suit):
             super().__init__(suit)
             
        def bid(self, value):
            self.cards.remove(value)
            return value