import random

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def printCard(self):
        print("{} of {}".format(self.value, self.suit))
class Deck:
    def __init__(self,cards):
        self.cards = []
        self.build()
        
    def build(self):
        self.cards = list(range(2,13) * 4)
class Player:
 def __init__(self):
        pass

class War:
     def __init__(self):
        pass


if __name__ == "__main__":
    card = Card("diamonds",5)
    card.printCard()