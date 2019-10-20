import time
from random import randint

class Game():
    def __init__(self):
        playing = True

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __str__(self):
        return f'{self.value} of {self.suit} '

class Player():
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.hand = []

class Deck():
    def __init__(self):
        # building deck of cards with nested for loop:
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['C', 'D', 'H', 'S']
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def deal_card(self, player, quantity=1):
        for num in range(0, quantity):
            player.hand.append(self.cards.pop(randint(0, len(self.cards))))

playing = True

while playing:
    player_name = input("Please type your name ")

    player = Player(name=player_name)
    dealer = Player(name='Dealer')

    # Display dealer's and player's cards:
    print('\n')
    print(f'{dealer.name} has {dealer.hand}')
    print(f'{player.name} has {player.hand}', '\n')

    time.sleep(1)

    # Placeholder for actual game logic
    print("Pretend we played a game...", '\n')
    deck = Deck()
    for card in deck.cards:
        print(card)

    # testing deck.deal()
    print(f"{player.name}'s hand before dealing cards = ")
    for card in player.hand:
        print(card, end='')

    print('\n')

    print(f"Cards in deck before dealing cards =", end=" ")
    for card in deck.cards:
        print(card, end='')

    deck.deal_card(player, 2)

    print('\n', f"{player.name}'s hand after dealing cards =", end=" ")
    for card in player.hand:
        print(card, end='')
    print('\n', '\n')
    print(f"Cards in deck after dealing cards =", end=" ")
    for card in deck.cards:
        print(card, end='')

    # Is it time to break out of the main game loop?
    play_again = input("Would you like to play again? (y/n) ")

    if play_again == 'n':
        playing = False


# TODO:
# handling aces: if aces in hand and total over 21, subtract 10 times the number of aces.
