import random
class Card:
    """represents a standard playing card"""

    def __init__(self, suit, rank):           # we can attach attributes to any instance through a number, which can then be indexed by the class variables for the corresponding card name
        self.suit = suit
        self.rank = rank

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank 

    def to_tuple(self):
        return (self.suit, self.rank)        # first element is the instance's suit, second element is the instance's rank

    def __lt__(self, other):
        return self.to_tuple() < other.to_tuple()
    
    def __le__(self, other):
        return self.to_tuple()<= other.to_tuple()

    def __str__(self):
        rank_name = self.rank_names[self.rank]
        suit_name = self.suit_names[self.suit]
        return f'{rank_name} of {suit_name}'

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

queen = Card(1,12)
six = Card(1,6)
class Deck:
    """represents a deck of cards"""

    def __init__(self, cards):
        self.cards = cards

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)                # prints cards in a list format, newline for each card
    
    def __len__(self):
        return len(self.cards)

    @staticmethod
    def make_cards():                     # static method not associated with any instance, but can be called on the class itself 
        cards = []
        for suit in range(4):
            for rank in range(2,15):
                cards.append(Card(suit,rank))
        return cards                      # returns full deck because it enumerates through all cards, although we could also make a smaller deck by a new method with only queen, aces, spades etc
    
    def take_card(self):
        return self.cards.pop()

    def put_card(self, card):
        return self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards.sort()

    def move_cards(self, other, num):
        for i in range(num):
            card = self.take_card()
            other.put_card(card)

cards = Deck.make_cards()
deck = Deck(cards)
small_deck = Deck([queen, six])
card = deck.take_card()        # takes a card from the deck instance and returns it
deck.put_card(card)          
deck.shuffle()
deck.sort()

class Hand(Deck):                           # Inherits from the deck class, so we can use all the methods of the deck class (or override them safely)
    """represents a hand of cards"""

    def __init__(self, label = ''):
        self.cards = []
        self.label = label
    
class BridgeHand(Hand):
    """ represents a bridge hand"""

    hcp_dict = {
        'Ace': 4,
        'King': 3,
        'Queen': 2,
        'Jack': 1
    }

    def hc_pointcount(self):
        count = 0
        for card in self.cards:
            rank_name = Card.rank_names[card.rank]
            count += BridgeHand.hcp_dict.get(rank_name, 0)         # gets value through using the key of rank_name in the hcp_dict, if not found, defaults to 0
        return count

hand = BridgeHand('player 2')
deck.shuffle()
deck.move_cards(hand, 5)
hand.move_cards(deck, 5)

class Trick(Deck):                                                 # subclass of deck so can use all methods
    """represents a trick in a card game"""
    cardlist = [ Card(1,3),                                        # accesses card init
              Card(1,10),
              Card(1,12),
              Card(2,13)]
    
    def findwinner(self):                                          # self.cards is a list of cards in the trick, created through the deck types init method 
        winner = self.cards[0]
        for card in self.cards:
            if card.suit == self.cards[0].suit and card.rank > winner.rank:      # accesses suit and rank from the card class
                winner = card
        return winner

trick = Trick(Trick.cardlist)                                       # creates a trick with the cardlist, accessing the cardlist class variable through the Trick classname
# print(trick.findwinner())
      
class PokerHand(Hand):
    """represents a poker hand"""

    def get_suit_counts(self):
        counter = {}
        for card in self.cards:
            key = card.suit
            counter[key] = counter.get(key, 0) + 1
        return counter 
    
    def get_rank_counts(self):
        counter = {}
        for card in self.cards:
            key = card.rank
            counter[key] = counter.get(key, 0) + 1
        return counter
    
    def has_flush(self):
        for key, value in self.get_suit_counts().items():             # dictionary to iterate through keys AND values
            if value >=5:
                return 'Flush'
        return False
    
    def has_straight(self):
        count = 0
        rank = self.cards[0].rank
        for i in range(len(self.cards)):
            rank = self.cards[i].rank -1
            if self.cards[i].rank == rank+1:
                count +=1
            else:
                count = 0
        return count >=5
    
    def straightflush(self):
        return self.has_flush() and self.has_straight()

    def pair(self):
        for key, value in self.get_rank_counts().items():
            if value >= 2:
                return 'Pair'
        return False

    def fullhouse(self):
        three = 0
        two = 0
        for key, value in self.get_rank_counts().items():
            if value == 3:
                three = 1
            if value == 2:
                two = 1
        print(three, two)
        return three == 1 and two == 1

hand = PokerHand('hand 1')
deck.shuffle()
deck.move_cards(hand, 7)
hand.move_cards(deck, 7)
deck.move_cards(hand, 7)
hand.move_cards(deck, 7)
hand = PokerHand('hand 2')
hand2 = PokerHand('hand 2')
hand2.cards = [Card(1,5),
              Card(1,5),
              Card(1,5),
              Card(2,10),
              Card(2,10)]
#print(hand2.fullhouse())
# print(hand2.straightflush())
# print(hand2.pair())