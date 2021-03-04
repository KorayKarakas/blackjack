import random
 
class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __repr__(self):
        return "%s %s" % (self.suit, self.rank)
 
    def __str__(self):
        return "%s of %s" % (self.rank, self.suit)
 
    def make_deck():
        deck = []
        suits = ["Diamonds", "Hearts", "Clubs", "Spades"]
        ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
 
        for i in suits:
            for j in ranks:
                deck.append(Card(i,j))
        random.shuffle(deck)
        return deck
 
    def value(self):
        if self.rank == "A":
            return (11) 
        elif self.rank == "J" or self.rank == "Q" or self.rank == "K":
            return 10  
        elif isinstance(self.rank, int):
            return self.rank  
        else:
            raise ValueError(f"Invalid rank: {self.rank}")
            
    
    
def draw_player():
    p = deck.pop()
    player.append(p)
    Card.value(p)
    player_value.append(Card.value(p))
    print("Player Hand: ", player)
    return player
 
def draw_dealer():
    q = deck.pop()
    dealer.append(q)
    Card.value(q)
    dealer_value.append(Card.value(q))
    print("Dealer Hand: ", dealer)
    return dealer
 
 
def calc_player():
    total = 0
    for val in player_value:
        total +=  val
        if (val == 11) and total > 21:
            total -= 10
    return total
 
def calc_dealer():
    tot = 0
    for val in dealer_value:
        tot +=  val
        if (val == 11) and tot > 21:
            tot -= 10
    return tot
 
 
 
def play():
    
    while True:
 
        start = input("Would you like to play Blackjack? [Yes/No]")
 
        if start.lower() == 'yes':
 
            draw_player()
            draw_dealer()
            draw_player()
 
            player_points = calc_player()
            dealer_points = calc_dealer()
 
            hitstand = input("Would you like to hit or stand?")
 
            if hitstand.lower() == 'hit':
 
                draw_player()
                player_points = calc_player()
 
                if player_points == 21:
                    while True:
                        draw_dealer()
                        dealer_points = calc_dealer()
                        if dealer_points == 21:
                            print("The game ends a Draw.")
                            return
                        elif (17 <= dealer_points < 21):
                            print('Player wins!')
                            return
                        elif dealer_points > 21:
                            print("Dealer Bust.")
                            return
                        elif dealer_points < 17:
                            draw_dealer()
                            dealer_points = calc_dealer()
 
                elif player_points <= 20:
 
                    while True:
 
                        hitstand = input("Would you like to hit or stand?")
                        if hitstand.lower() == 'hit':
                            draw_player()
                            player_points = calc_player()

                            if player_points == 21:
                                draw_dealer()
                                dealer_points = calc_dealer()

                                if dealer_points == 21:
                                    print("The game ends a Draw.")
                                    return

                                elif (17 <= dealer_points < 21):
                                    print('Player wins!')
                                    return

                                elif dealer_points > 21:
                                    print("Dealer Bust.")
                                    return

                                elif dealer_points < 17:
                                    draw_dealer()
                                    dealer_points = calc_dealer()

                            elif player_points > 21:
                                draw_dealer
                                dealer_points = calc_dealer()
                                print("BUST!!! Dealer Wins.")
                                return
 
                        elif hitstand.lower() == 'stand':
 
                            player_points = calc_player()
                            draw_dealer()
                            dealer_points = calc_dealer()
 
                            while True:
 
                                if (dealer_points > player_points) and (dealer_points <= 21):
                                    print("Dealer Wins.")
                                    return

                                elif (dealer_points < 17) and (dealer_points < player_points):
                                        draw_dealer()
                                        dealer_points = calc_dealer()
 
                                elif (dealer_points < player_points) and (17 <= dealer_points < 21):
                                    print("Player Wins.")
                                    return

                                elif dealer_points == player_points:
                                    print("Game is a Draw.")
                                    return

                                elif dealer_points > 21:
                                    print("Dealer Bust. Player Wins.")
                                    return
 
 
                elif player_points > 21:
                    draw_dealer()
                    dealer_points = calc_dealer()
                    print("BUST!!! Dealer Wins.")
                    return
 
            elif hitstand.lower() == 'stand':
 
                player_points = calc_player()
                draw_dealer()
                dealer_points = calc_dealer()
                while True:
 
                    if (dealer_points > player_points) and (dealer_points <= 21):
                        print("Dealer Wins.")
                        return

                    elif (dealer_points < 17) and (dealer_points < player_points):
                            draw_dealer()
                            dealer_points = calc_dealer()
 
                    elif (dealer_points < player_points) and (17 <= dealer_points < 21):
                        print("Player Wins.")
                        return

                    elif dealer_points == player_points:
                        print("Game is a Draw.")
                        return

                    elif dealer_points > 21:
                        print("Dealer Bust. Player Wins.")
                        return
 
        elif start.lower() == 'no' :
            print("Maybe next time")
        else:
            print("Sorry that wasn't a yes or no, please try again.")
        return
 
 
if __name__ == "__main__":
    while True:
        player = []
        player_value = []
        dealer = []
        dealer_value = []
        deck = Card.make_deck()
        play()

 
 