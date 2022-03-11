import random

class Card:
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def printCard(self):
        print("{} of {}".format(self.value,self.suit))
class Deck:
    def __init__(self):
        self.cards = list(range(2,15)) * 4
        for suit in ['Hearts','Diamonds','Spades','Clubs']:
            for value in range(1,14):
                self.cards.append(Card(suit,value))

        random.shuffle(self.cards)

    def printDeck(self):
        print(self.cards)
class Player:
    def __init__(self,name):
        self.wins = 0
        self.card = None
        self.name = name
        pass

class War:
    def __init__(self):
            self.deck = Deck()
            self.player1 = Player("CPU")
            self.player2 = Player(input("Enter your name: "))
    
    def start_war():
        return


if __name__ == "__main__":
    game = War()
    game.start_war()
