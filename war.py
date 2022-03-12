import random
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
            return -1
        return self.playerDeck.pop()
    
class War:
    def __init__(self):
            self.deck = Deck()
            half1 = self.deck.cards[:26]
            half2 = self.deck.cards[26:]
            self.player1 = Player("CPU",half1)
            self.player2 = Player(input("Enter your name: "),half2)
            self.wars = 0
            self.rounds = 0

    def start_war(self):
        
        print("\nLet The Battle Begin!")
        player1Cards_onTable = []
        player2Cards_onTable = []

        while self.player1.playerDeck and self.player2.playerDeck:
    
            self.rounds += 1

            
            p1FightingCard = self.player1.drawCard()
            p2FightingCard = self.player2.drawCard()

            print("{} drew card of value {}, {} drew card of value {}".format(self.player1.name, p1FightingCard, self.player2.name, p2FightingCard))    
            print("Round: ",self.rounds)

            # print("CPU has {} cards. \n".format(len(self.player1.playerDeck)))
            # print("{} has {} cards \n".format(self.player2.name,len(self.player2.playerDeck)))
            

            if (p1FightingCard == p2FightingCard): # War logic 
                print("There are equal fighters... WAR!\n")
                self.wars += 1

                
                player1Cards_onTable.extend([p1FightingCard] + self.player1.playerDeck[-3:])  #Draw 3 cards and add it to table along with card in hand
                self.player1.playerDeck = self.player1.playerDeck[:-3]                        #Remove top 3 cards from deck

                player2Cards_onTable.extend([p2FightingCard] + self.player2.playerDeck[-3:])  #Draw 3 cards and add it to table along with card in hand
                self.player2.playerDeck = self.player2.playerDeck[:-3]                        #Remove top 3 cards from deck

            
            elif (p1FightingCard > p2FightingCard):

                #Winner adds the card to the bottom of the deck.
                self.player1.playerDeck = [p1FightingCard] + [p2FightingCard] + player1Cards_onTable + player2Cards_onTable + self.player1.playerDeck
                #Clear the table of any cards
                player1Cards_onTable = []
                player2Cards_onTable = []

            else:

                #Winner adds the card to the bottom of the deck.
                self.player2.playerDeck = [p1FightingCard] + [p2FightingCard] + player1Cards_onTable + player2Cards_onTable + self.player2.playerDeck
                #Clear the table of any cards
                player1Cards_onTable = []
                player2Cards_onTable = []
        
        if(len(self.player1.playerDeck) == 0): 
                if(len(self.player2.playerDeck) == 0):
                    print("Both players have ran out of cards, it is a draw...")
                else:
                    print("The Battle is Over, {} has no more cards to fight, {} is the Victor...".format(self.player1.name,self.player2.name))  
        else:
                 print("The Battle is Over, {} has no more cards to fight, {} is the Victor...".format(self.player2.name,self.player1.name))\

        print("The Battle Lasted for {} Rounds and There Were {} Wars!".format(self.rounds,self.wars))
        print("CPU has {} cards. \n".format(len(self.player1.playerDeck)))
        print("{} has {} cards \n".format(self.player2.name,len(self.player2.playerDeck)))
        print("The rest were lost in the battle field...")

if __name__ == "__main__":

    game = War()
    game.start_war()

