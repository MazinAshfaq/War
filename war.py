"""
Mazin Ashfaq
War game in Python
3/12/2022

This is an implementation of the card game in python using some OOP techniques.
The game is played against the CPU and plays out until one player is left with no cards
"""
import random
class Deck:
    def __init__(self):
        """
        Constructor for creating a deck
        """
        self.cards = list(range(2,15)) * 4
        random.shuffle(self.cards)

class Player:
    def __init__(self,name,playerDeck):
        """
        Constructor for creating a player 
        """
        self.wins = 0
        self.playerDeck = playerDeck
        self.name = name
    
    def drawCard(self):
        """
        This is the function that returns a card from top of the deck
        """
        return self.playerDeck.pop()
    
class War:

    def __init__(self):
            """
            Constructor for creating a war object
            """
            self.deck = Deck()
            half1 = self.deck.cards[:26] #Spit Deck for each player
            half2 = self.deck.cards[26:] #Spit Deck for each player
            self.player1 = Player("CPU",half1)
            self.player2 = Player("Mazin",half2)
            self.wars = 0
            self.rounds = 0

    def start_war(self):
        """
        This is the function that does the logic for the card game
        """

        print("\nLet The Battle Begin!")

        #Create table to hold cards in play
        player1Cards_onTable = []
        player2Cards_onTable = []

        #This loops breaks if either player runs out of cards, leading to a win condition
        while self.player1.playerDeck and self.player2.playerDeck:   
            self.rounds += 1

            #Draw cards from top of the deck
            p1FightingCard = self.player1.drawCard()
            p2FightingCard = self.player2.drawCard()

            print("{} drew card of value {}, {} drew card of value {}".format(self.player1.name, p1FightingCard, self.player2.name, p2FightingCard))    
            print("Round: ",self.rounds)
            
            # War logic when cards are equal value
            if (p1FightingCard == p2FightingCard): 
                print("There are equal fighters... WAR!\n")
                self.wars += 1

                
                player1Cards_onTable.extend([p1FightingCard] + self.player1.playerDeck[-3:])  #Draw 1 cards and add it to table along with card in hand
                self.player1.playerDeck = self.player1.playerDeck[:-3]                        #Remove top cards from deck

                player2Cards_onTable.extend([p2FightingCard] + self.player2.playerDeck[-3:])  #Draw cards and add it to table along with card in hand
                self.player2.playerDeck = self.player2.playerDeck[:-3]                        #Remove top cards from deck

            #If player 1 has a stronger card
            elif (p1FightingCard > p2FightingCard):

                #Winner adds the card to the BOTTOM of the deck.
                self.player1.playerDeck = [p1FightingCard , p2FightingCard] + player1Cards_onTable + player2Cards_onTable + self.player1.playerDeck

                #Clear the table of any cards
                player1Cards_onTable = []
                player2Cards_onTable = []

            #If plyer 2 has a stronger card
            else:

                #Winner adds the card to the BOTTOM of the deck.
                self.player2.playerDeck = [p2FightingCard , p1FightingCard] + player2Cards_onTable + player1Cards_onTable +  self.player2.playerDeck

                #Clear the table of any cards
                player1Cards_onTable = []
                player2Cards_onTable = []
        
        #Win Conditions and printing after loop has completed
        if(len(self.player1.playerDeck) == 0): 
                #Second check to account if there is a draw
                if(len(self.player2.playerDeck) == 0):
                    print("Both players have ran out of cards, it is a draw...")
                else:
                    print("\nThe Battle is Over, {} has no more cards to fight, {} is the Victor...".format(self.player1.name,self.player2.name))  
        else:
                 print("\nThe Battle is Over, {} has no more cards to fight, {} is the Victor...".format(self.player2.name,self.player1.name))\

        #Print game details
        print("\nThe Battle Lasted for {} Rounds and There Were {} Wars!".format(self.rounds,self.wars))
        print("CPU has {} cards. \n".format(len(self.player1.playerDeck)))
        print("{} has {} cards \n".format(self.player2.name,len(self.player2.playerDeck)))
        print("The rest were lost in the battle field...")

if __name__ == "__main__":
    """
    Main function to create a game of war and call it
    """
    game = War()
    game.start_war()

