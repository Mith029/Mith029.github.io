from random import shuffle 

signs = ('Hearts', 'Diamonds', 'Spades', 'clubs')
ranks = ('Ace', 'Two', 'Three', 'Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King')
values = {'Ace': 11,'Two': 2, 'Three': 3, 'Four': 4,'Five': 5,'Six': 6,'Seven': 7,'Eight': 8,'Nine': 9,'Ten': 10,'Jack': 10,'Queen': 10,'King': 10}
playing = True 

class Card:
    def __init__(self, sign, rank):
        self.sign = sign
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return str(self.rank) + ' of ' + str(self.sign)

class Deck:
    def __init__(self):
        self.deck = []
        
        for sign in signs:
            for rank in ranks:
                deck_of_cards = Card(sign, rank)
                self.deck.append(deck_of_cards)
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has:' + deck_comp 

    def shuffle(self):
        shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card
        
class Chips():
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet
        
class Hand(): 
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_aces(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('how many chips would you like to bet: '))
        except:
            print('Oops! please provide an integer.')
        else:
            if chips.bet > chips.total:
                print(f'Woops! Insufficient chips. You have {chips.total} chips.')
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()
    
def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input('Hit or Stand? Enter h for hit or s for stand')
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player stands! Dealer's turn")
            playing = False
        else:
            print('Sorry, I did not understand that. Enter h or s: ')
            continue 
        break
        
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
def player_busts(player, dealer, chips):
    print('Player Bust!')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player Wins!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('Dealer Bust!')
    chips.lose_bet()
    
def dealer_wins(player, dealer, chips):
    print('Dealer Wins!')
    chips.win_bet()
    
def push(player, dealer):
    print('Player and Dealer tie! PUSH.')

var = True
while var:# Welcome message
    print('Welcome to Black Jack!')

    #create deck and then shuffle
    deck = Deck()
    deck.shuffle()

    #divide the cards for the player and the dealer
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #set up player's chip
    player_chips = Chips()

    #prompt the player for their bet
    take_bet(player_chips)

    #show cards
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    

            # Show all cards
        show_all(player_hand, dealer_hand)
            # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)


        # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)

        # Ask to play again
    new_game = ''
    while new_game not in ['y','n']:
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
        
        if new_game[0].lower()=='y':
            playing=True
            continue
        if new_game[0].lower()=='n':
            print("Thanks for playing!")
            var = False
            break