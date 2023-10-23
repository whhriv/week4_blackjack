import random
suit = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
rank = ('two', 'three', 'four', 'five','six', 'seven', 'Eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
values = {'two':2, 'three': 3, 'four':4, 'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10, 'jack':10, 'queen':10, 'king':10, 'Ace': 11}

playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):

        return self.rank + ' of ' + self.suit
    
class Deck:
    def __init__(self):
        self.deck = []
        for i in suit:
            for r in rank:
                self.deck.append(Card(i,r))

    def shuffle(self): 
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0 #keep track
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'ace':
            self.aces +=1

    def aces(self):
        while self.value > 21 and self.aces:
            self.value -= 1
            self.aces -= 1

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    def lost_bet(self):
        self.total -= self.bet

def take_bets(chips):
    while True:
        chips.bet = int(input("how much you got?"))

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.aces()

def hit_or_stay(deck, hand):
    global playing
    while True:
        ask = input("hit or stay, 'h or s'")
        if ask[0].lower()  ==  'h':
            hit(deck, hand)
        elif ask[0] == 's':
            print('player stay')
            playing = False
        else:
            print('wrong input')
            continue
            break

def display_card(player, dealer):
    print("dealer's hand, " , dealer.card[1])
    print("player's hand:" *player.card)


def display_all(player, dealer):
    print("dealers hand:", *dealer.card)
    print("dealers hand", dealer.value)
    print("player hand:", *player.card)
    print("player hand:", player.value)

#ending game

def player_bust(player, dealer, chips):
    print("player bust")
    chips.lost_bet()

def player_wins(player, dealer, chips):
    print('dealer bust')
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("dealer win")
    chips.lose_bet()

def tie(player, dealer):
    print("player and dealer same value")

#playing


player_hand = Hand()
player_hand.add_card(Deck.deal())

while True:
    print("Start making bad decisions")

    #built/shuffle deck
    deck = Deck()
    player_hand.add_card()
    player_hand.add_card()

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # player_hand = Hand()
    # player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bets(player_chips)

    disply_card(player_hand, dealer_hand)

    while playing:

        hit_or_stay(deck, player_hand)
        display_card(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

    print("player has chips", player_chips.total)

    new_game = input("Play again? y/n")
    if new_game[0] == 'y':
        playing = True
        continue
    else: 
        print("stopped playing")
        break