# Blackjack

This is a standard casino style blackjack game between a player and a dealer (CPU), made using classes, methods and loops in Python. Each card is defined by a suit and a rank it's assigned to and a corresponding value is calculated. A deck of 52 cards is then instantiated in configurations of a conventional deck of playing cards and the deck is then shuffled. 

# Rules

Conforming to the rules of casino style blackjack, the player gets dealt a hand and is presented the option of either hitting or standing. If the player chooses to hit, another card is drawn and the player is asked again. The player is allowed to choose hit until they reach a score greater than 21, in which case they bust and lose the game. 

The dealer is also dealt cards and given that the player chose to stand, if the dealer's score is higher within the legal parameters, the dealer wins the game. If the dealer's hand equals a total of 17 or above, and is less than the player's hand, the player wins. However if the dealer's hand is less than 17 and below the player's hand, the dealer must continue drawing cards until it either busts, wins or reaches the previous condition and loses the game. 
