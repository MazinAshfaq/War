import random

from numpy import half

# class Card:
#     def __init__(self, suit, value):
#         self.value = value
#         self.suit = suit

#     def printCard(self):
#         print("{} of {}".format(self.value,self.suit))
class Deck:
    def __init__(self):
        self.cards = list(range(2,15)) * 4
        random.shuffle(self.cards)
    
    def drawCard(self):
        if (len(self.cards) == 0):
            return
        return self.cards.pop()

class Player:
    def __init__(self,name):
        self.wins = 0
        self.card = None
        self.name = name
    


class War:
    def __init__(self):
            self.deck = Deck()
            self.player1 = Player("CPU")
            self.player2 = Player(input("Enter your name: "))

    
    def start_war(self):
        
        print("\nWar Has Started!")
        while (len(self.deck.cards) > 2):
        
            self.player1.card = self.deck.drawCard()
            self.player2.card = self.deck.drawCard()
            
            print("{} drew card of value {}, {} drew card of value {}".format(self.player1.name, self.player1.card, self.player2.name, self.player2.card))    




if __name__ == "__main__":
    game = War()
    game.start_war()
