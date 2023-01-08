#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

import random

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self, SUITE, RANKS):
        self.SUITE = SUITE
        self.RANKS = RANKS

    def shuffle(self, item):
        random.shuffle(item)
        return item

    def card(self):
        self.CARDS = list()
        for (i, s) in enumerate(self.SUITE):
            for (j, r) in enumerate(self.RANKS):
                self.CARDS.append([s, j])
        self.CARDS = self.shuffle(self.CARDS)
        return self.CARDS

    def split(self):
        self.CARDS = self.card()
        self.half = len(self.CARDS)//2
        return self.CARDS[:self.half], self.CARDS[self.half:]


class Hand(Deck):
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, player, SUITE, RANKS):
        self.player = player
        Deck.__init__(self, SUITE, RANKS)
        self.machine_card = list()
        self.human_card = list()

    def distribute(self):
        self.human_card, self.machine_card = Deck.split(self)
        #print(self.human_card, len(self.human_card))
        #print(self.machine_card, len(self.machine_card))

    def war(self, round = 1):
        if len(self.human_card) > round*3 and len(self.machine_card) > 3*round:
            if self.human_card[3*round][1] < self.machine_card[3*round][1]:
                return False, round
            elif self.human_card[3*round][1] > self.machine_card[3*round][1]:
                return True, round
            else:
                return self.war(round = round + 1)
        else:
            if len(self.human_card) < round*3:
                if self.human_card[len(self.human_card)-1][1] <= self.machine_card[len(self.human_card)-1][1]:
                    return False, round
                elif self.human_card[len(self.human_card)-1][1] > self.machine_card[len(self.human_card)-1][1]:
                    return True, round
            elif len(self.machine_card) < round*3:
                if self.human_card[len(self.machine_card)-1][1] < self.machine_card[len(self.machine_card)-1][1]:
                    return False, round
                elif self.human_card[len(self.machine_card)-1][1] >= self.machine_card[len(self.machine_card)-1][1]:
                    return True, round

    def validate(self):
        if self.machine_card[0][1] > self.human_card[0][1]:
            self.machine_card.append(self.human_card.pop(0))
        elif self.machine_card[0][1] < self.human_card[0][1]:
            self.human_card.append(self.machine_card.pop(0))
        else:
            self.isHumanWins, self.round = self.war()
            if self.isHumanWins:
                for r in range((self.round*3) + 1):
                    if len(self.machine_card) > 0:
                        self.human_card.append(self.machine_card.pop(0))
            else:
                for r in range((self.round*3) + 1):
                    if len(self.human_card) > 0:
                        self.machine_card.append(self.human_card.pop(0))


class Player(Hand):
    def __init__(self, player, SUITE, RANKS):
        self.player = player
        Hand.__init__(self, player, SUITE, RANKS)
        self.distribute()
        #Hand.distribute(self)

    def play(self):
        while len(self.machine_card) != 0 and len(self.human_card) != 0:
            self.validate()
            #Hand.validate(self)
        if len(self.machine_card) == 0:
            print('Congrats, you win!')
        elif len(self.human_card) == 0:
            print('Oops, you loss.')


######################
#### GAME PLAY #######
######################
def main():
    print("Welcome to War, let's begin...")
    player = Player(str(input('Enter your name: ')), SUITE, RANKS)
    player.play()

main()

# Use the 3 classes along with some logic to play a game of war!
