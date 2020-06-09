import random

suits = {'Hearts', 'Diamonds', 'Spades', 'Clubs'}
ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'}
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck():
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank)) # card = Card(suit,rank)
                                 
    def __str__(self):
        listOfCards = 'Deck includes the following:\n'
        for cards in self.deck:
            listOfCards += '\n'+cards.__str__()
        return listOfCards

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        deal_card = self.deck.pop()
        return deal_card

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        print(f'{card} added to hand!')
        self.value += values[card.rank]
        print(f'Total value of hand: {self.value}')
        
        #track aces
        if card.rank == 'Ace': # add counter for aces
            self.aces += 1
        
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.aces -= 1
            self.value -= 10

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips are you betting today? '))
                           
        except ValueError:
            Print('Please provide us with a number for your bet...')
                           
        else:
            if(chips.bet > chips.total):
                print('Your bet is insufficient. Please input another value')
            else:
                break

def hit(deck,hand):
    #add card from deck
    hand.add_card(deck.deal())
    #adjust for ace if necessary
    hand.adjust_for_ace()

def hit_or_stand(deck,player):
    global playing  # to control an upcoming while loop
    
    while True:
        prompt = input('Would you like to [H]it or S[tand]?:')
        
        if prompt[0].lower() == 'h':
            hit(deck,player)
            
        elif prompt[0].lower() == 's':
            print('Player stands.... Dealer is now playing.')
            playing = False
            
        else:
            print('You have provided an incorrect value. Please try again...')
            continue 
            
        break

def show_some(player,dealer):
    print(f'Player Hand: ')
    for card in player.cards:
        print(f'|{card}|')

    print('Dealer Hand: ')
    print(f'Cards:|{dealer.cards[1]}|')

def show_all(player,dealer):
    print('Player Hand: ')
    for card in player.cards:
        print(f'Cards: |{card}|')
    print(f'Value: {player.value}')
    
    print('Dealer Hand: ')
    for card in dealer.cards:
        print(f'Cards:|{card}|')
    print(f'Value: {dealer.value}')

def player_busts(hand,chips):
     print(f'Sorry, your hand is at {player.value}. It is a bust! You lost {chips.bet} chips.')
     chips.lose_bet()
    
def player_wins(chips):
    print(f'Congratulations! You beat the dealer! You have received {chips.bet} chips.')
    chips.win_bet()

def dealer_busts(hand,chips):
     print(f'Dealer hand is at {dealer.value}. It is a bust! You win {chips.bet} chips.')
     chips.win_bet()
    
def dealer_wins(chips):
    print(f'Dealer wins. You lose {chips.bet} chips')
    chips.lose_bet()
    
def push():
    print('Dealer and Player have tied.')

while True:
    # Print an opening statement
    print('Welcome to the ultimate Black Jack game!')
    
    # Create & shuffle the deck, deal two cards to each player    
    deck = Deck()
    deck.shuffle()
    
    #Create player and dealer
    player = Hand()
    dealer = Hand()
    
    #Deal two cards to player and dealer
    player.add_card(deck.deal())
    player.add_card(deck.deal())
    
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())
    
        
    # Set up the Player's chips
    player_chips = Chips()
    
    
    # Prompt the Player for their bet
    take_bet(player_chips)

    
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player,player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21:
        while dealer.value < 17:
            hit(deck,dealer)
        
        # Show all cards
        show_all(player,dealer)
        
        # Run different winning scenarios

        if dealer.value > 21:
            dealer_busts(dealer,player_chips)

        elif player.value > dealer.value:
            player_wins(player_chips)

        elif player.value < dealer.value:
            dealer_wins(player_chips)

        else:
            push()
    
    # Inform Player of their chips total 
    print(f'Player has {player_chips.total} chips available.')
    
    #Ask player if they want to replay
    replay = input('Would you like to play again? [Y/N]').lower()
    if(replay[0] == 'y'):
        playing = True
        continue
    else:
        print('Thank you for playing!')
        break