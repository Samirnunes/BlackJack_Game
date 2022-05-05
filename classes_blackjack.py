import random

suits = ('s', 'c', 'h', 'd') # s: spades ; c:clubs ; h:hearts ; d:diamonds
rankings = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J') # A: Ace ; K: King ; Q: Queen ; J: Jack

card_val = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10 , 'K': 10, 'Q': 10, 'J':10}

class card():
    def __init__(self, suit, ranking):
        self.suit = suit
        self.rank = ranking
    
    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank
    
    def card_value(self):
        return card_val[self.get_rank()]

class deck():
    def __init__(self):
        global suits, rankings
        self.cards = []
        for suit in suits:
            for rank in rankings:
                self.cards.append(card(suit,rank))

    def shuffle(self):
        random.shuffle(self.cards)

    def remove_card(self):
        removed_card = self.cards.pop()
        return removed_card

class hand():
    def __init__(self):
        self.cards = []
        self.soft_value = 0
        self.hard_value = 0

    def draw(self, card):
        if card.get_rank() == 'A':
            self.soft_value += card.card_value() + 10
            self.hard_value += card.card_value()
        else:
            self.soft_value += card.card_value()
            self.hard_value += card.card_value()
        self.cards.append(card)

    def get_soft_value(self):
        return self.soft_value

    def get_hard_value(self):
        return self.hard_value

    def play_value(self):
        if self.soft_value <= 21:
            return self.soft_value
        else:
            return self.hard_value

class player(hand):
    def print_hand_cards(self):
        for i in range(0, len(self.cards)):
            print('## ' + self.cards[i].get_suit() + self.cards[i].get_rank() + ' ##')
    
    def shown_play_value(self):
        return self.play_value()
    

class dealer(hand):
    def print_hand_cards(self):
        for i in range(1, len(self.cards)):
            print('## ' + self.cards[i].get_suit() + self.cards[i].get_rank() + ' ##')

    def shown_play_value(self):
        if self.cards[0].get_rank() == 'A':
                return self.soft_value - 11
        else:
            return self.play_value() - self.cards[0].card_value()