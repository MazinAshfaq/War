import random

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

class Player:
    def __init__(self,name,playerDeck):
        self.wins = 0
        self.playerDeck = playerDeck
        self.name = name
    
    def drawCard(self):
        if (len(self.playerDeck) == 0):
            return
        return self.playerDeck.pop()
    


class War:
    def __init__(self):
            self.deck = Deck()
            half1 = self.deck.cards[:26]
            half2 = self.deck.cards[26:]
            self.player1 = Player("CPU",half1)
            self.player2 = Player(input("Enter your name: "),half2)

    def compare(card1,card2):
        if card1 == card2:
            return 0
        elif card1 > card2:
            return 1
        else:
            return 2

    def start_war(self):
        
        print("\nWar Has Started!")
        rounds = 0
        player1Cards_onTable = []
        player2Cards_onTable = []

        while self.player1.playerDeck and self.player2.playerDeck:
            rounds += 1

            
            player1Cards_onTable.append(self.player1.drawCard())
            player2Cards_onTable.append(self.player2.drawCard())
            
            print("{} drew card of value {}, {} drew card of value {}".format(self.player1.name, player1Cards_onTable[-1], self.player2.name, player2Cards_onTable[-1]))    
            print("Round: ",rounds)




if __name__ == "__main__":
    game = War()
    game.start_war()

    # deck = Deck()
    # print(deck.cards)
    # deckhalf1 = deck.cards[:26]
    # deckhalf2 = deck.cards[26:]
    # print(deckhalf1)
    # print(deckhalf2)
