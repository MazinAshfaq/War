# War (card game) implemented in python!

##War for two players rules
In the basic game there are two players and you use a standard 52 card pack. Cards rank as usual from high to low: A K Q J T 9 8 7 6 5 4 3 2. Suits are ignored in this game.

Deal out all the cards, so that each player has 26. Players do not look at their cards, but keep them in a packet face down. The object of the game is to win all the cards.

Both players now turn their top card face up and put them on the table. Whoever turned the higher card takes both cards and adds them (face down) to the bottom of their packet. Then both players turn up their next card and so on.

If the turned up cards are equal there is a war. The tied cards stay on the table and both players play the next card of their pile face down and then another card face-up. Whoever has the higher of the new face-up cards wins the war and adds all six cards face-down to the bottom of their packet. If the new face-up cards are equal as well, the war continues: each player puts another card face-down and one face-up. The war goes on like this as long as the face-up cards continue to be equal. As soon as they are different the player of the higher card wins all the cards in the war.

The game continues until one player has all the cards and wins. This can take a long time.

If you don't have enough cards to complete the war, you lose. If neither player has enough cards, the one who runs out first loses. If both run out simultaneously, it's a draw. Example: Players A and B both play sevens, so there is a war. Each player plays a card face down, but this is player B's last card. Player A wins, since player B does not have enough cards to fight the war.


##Assumptions
An assumptions that I made were that the order in which the winners cards are put into the deck does not matter as long as they are at the bottom of the deck. Another assumption I went with was when war occurs, three cards are placed and one more is compared to find the winner. There are multiple sets of rules, some of which say only one card needs to be drawn in war.

A corner case that I ran into was when adding winners cards back into the pile. In some cases it would result in infinit games. I fixed this by alternating the way the winning cards were placed into the deck, and this fixed the infinite games.

If given more time I would make the game more moduler by refactoring and creating more functions for repeated actions. I would also like to add a "card" class which would allow for keeping track of the suit, just for nice playability. Maybe even add a GUI which animations to let the player enjoy the game in action. 
