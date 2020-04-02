'''
Text-based blackjack game
'''
import random
import time


class Deck():
    '''
    Deck of 52 cards.
    Attributes:
        CARDS: a dictionary with all the cards and it's values
        SUITS: a list with all the suits in the deck (Hears, Diamonds,...)
        RANKS: a list with all the ranks, from A, 2, .. to Q, K
        deck: a list of tuples with all the combinations RANKS, SUITS (52 in total)
    Methods:
        shuffle_cards(): to randomly shuffle the list
        deal(): return one card and remove it from the deck
    '''
    CARDS = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
             '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

    SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.deck = deck = [(r, s) for s in self.SUITS for r in self.RANKS]

    def shuffle_cards(self):
        random.shuffle(self.deck)

    def deal(self):
        res = self.deck.pop()
        return (res[0], res[1], self.CARDS[res[0]])

    def __str__(self):
        return str(self.deck)


class Player():
    '''
    Player class to keep track of his cards, his chips and his bet
    Methods:
        add_card(): add a tuple with the suit and the rank to the list of
                    cards in one hand
    '''

    def __init__(self):
        self.cards = []   # list with all the cards in one hand
        self.value = 0   # value of the hand
        self.num_aces = 0  # number of aces so adjustments can be done
        self.win = False  # True when the player wins

    def initialize(self):
        self.cards = []   # list with all the cards in one hand
        self.value = 0   # value of the hand
        self.num_aces = 0  # number of aces so adjustments can be done

    def add_card(self, card):
        self.cards.append(card)
        self.value += card[2]
        if card[0] == 'A':
            self.num_aces += 1

    def validate_cards(self):
        if self.value > 21:
            if self.num_aces <= 0:
                return self.value
            else:
                for n in self.cards:
                    if n[2] == 11:
                        self.value -= 10
                        self.num_aces -= 1
                    if self.value <= 21:
                        break

        if self.value < 21:
            return self.value
        elif self.value == 21:
            self.win = True
            return self.value


class Human(Player):
    '''
    Human player class to keep track of his cards, his chips and his bet
    Methods:
        win_bet(): increase the chips with 1.5 times the bet and initialize
                   the bet to 0
        set_bet(): if the amount passed as bet is less than or equal to the
                   chips, the amount is subtracted from the chips and saved
                   into the bet variable. If there are not enough chips,
                   False is returned, True otherwise.
    '''

    def __init__(self):
        Player.__init__(self)
        self.chips = 100  # amount of chips available to bet
        self.bet = 0      # amount of the actual bet

    def win_bet(self):
        self.chips += int(self.bet * 1.5)
        self.bet = 0

    def restore_bet(self):
        self.chips += self.bet
        self.bet = 0

    def set_bet(self, amount):
        if self.chips >= amount:
            self.chips -= amount
            self.bet = amount
            return True
        else:
            return False

    def __str__(self):
        return f'Cards: {str(self.cards)}, chips: {self.chips}, bet: {self.bet}'


class Dealer(Player):
    '''
    Computer player (dealer) class to keep track of his cards
    Methods:
        show_card(): show the hidden card
    '''

    def __init__(self):
        Player.__init__(self)
        self.show_card = False  # indicates if the second card must be shown


def board(deck, human, dealer):
    '''
    Print the board of the game
    '''
    v_h = human.validate_cards()
    v_d = dealer.validate_cards()
    print('\n' * 100)
    print('        B L A C K J A C K')
    print('        -----------------')
    print()
    print('             DEALER')
    print('             ------')
    print()
    print('     ', end='')
    for i, card in enumerate(dealer.cards):
        if i == 1 and dealer.show_card == False:
            print(' X', end='  ')
        else:
            print(' ' + card[0], end='  ')
    print('\n     ', end='')
    for i, card in enumerate(dealer.cards):
        if i == 1 and dealer.show_card == False:
            print('XXX', end=' ')
        else:
            print(card[1][0:3], end=' ')
    print()
    print()
    print()
    print('DECK: {}'.format(len(deck)))
    print()
    print()
    print()
    print('             PLAYER')
    print('             ------')
    print('     ', end='')
    for card in human.cards:
        print(' ' + card[0], end='  ')
    print('\n     ', end='')
    for card in human.cards:
        print(card[1][0:3], end=' ')
    print()
    print(f'        Chips: {human.chips}  Bet: {human.bet}')
    print()
    print()
    return (v_d, v_h)


def ask_play_again():
    while True:
        repeat = input('Do you want to play again(y/n)? ')
        if repeat.lower().startswith('y'):
            return True
        elif repeat.lower().startswith('n'):
            return False
        else:
            continue


def ask_for_bet(p1):
    while True:
        try:
            bet = int(input('What is your bet? '))
        except:
            print('Please, enter a number!!!')
            continue
        else:
            if p1.set_bet(bet):
                print('Bet accepted!!!')
                break
            else:
                print('Not enough amount!! Try another bet!')
    return bet


def ask_for_hit():
    while True:
        hit = input('Hit or Stay(Hit/Stay)? ')
        if hit.lower().startswith('h'):
            return True
        elif hit.lower().startswith('s'):
            return False
        else:
            continue


def continue_hitting(dealer, human1):
    if human1.value > 21:
        return False

    if dealer.value < 21:
        if dealer.value > human1.value:
            return False
        else:
            return True
    elif dealer.value == 21:
        dealer.win = True
        return False
    else:
        return False


def initialize_players(dealer, human1):
    dealer.cards = []


def main():
    human1 = Human()
    dealer = Dealer()
    while True:
        d = Deck()
        d.shuffle_cards()
        board(d.deck, human1, dealer)
        bet = ask_for_bet(human1)
        if bet == 0:
            print('GOODBYE !!!!')
            break
        board(d.deck, human1, dealer)

        # deal two cards to the player and the dealer
        human1.add_card(d.deal())
        human1.add_card(d.deal())
        dealer.add_card(d.deal())
        dealer.add_card(d.deal())
        board(d.deck, human1, dealer)

        # KEEP ASKING THE PLAYER IF HE WANTS MORE CARDS
        while True:
            if human1.value > 21:
                break
            if not ask_for_hit():
                break

            human1.add_card(d.deal())
            board(d.deck, human1, dealer)

        # DEAL CARDS TO DEALER UNTIL WINS OR BUSTS
        dealer.show_card = True
        val_dealer, val_human = board(d.deck, human1, dealer)
        while True:
            if not continue_hitting(dealer, human1):
                break

            time.sleep(1)
            dealer.add_card(d.deal())
            val_dealer, val_human = board(d.deck, human1, dealer)

        # MESSAGES!!
        if val_dealer == val_human or (val_dealer > 21 and val_human > 21):
            print(f'DEALER: {val_dealer} - {val_human} PLAYER. NO WINNER!!!!')
            human1.restore_bet()
        elif val_dealer > 21:
            print(f'DEALER: {val_dealer} - {val_human} PLAYER. HUMAN WINS!!!!')
            human1.win_bet()
        elif val_human > 21:
            print(f'DEALER: {val_dealer} - {val_human} PLAYER. DEALER WINS!!!!')
            human1.bet = 0
        elif val_human > val_dealer:
            print(f'DEALER: {val_dealer} - {val_human} PLAYER. HUMAN WINS!!!!')
            human1.win_bet()
        elif val_human < val_dealer:
            print(f'DEALER: {val_dealer} - {val_human} PLAYER. DEALER WINS!!!!')
            human1.bet = 0

        dealer.initialize()
        dealer.show_card = False
        human1.initialize()

        if human1.chips <= 0:
            print('You have lost all your chips!!! Get out of here, loser!!!!')
            break

        repeat = ask_play_again()
        if not repeat:
            print('You have won {} chips!!!'.format(human1.chips))
            print('GOODBYE !!!!')
            break


if __name__ == '__main__':
    main()
