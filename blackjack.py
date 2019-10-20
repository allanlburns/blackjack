import time

class Game():
    def __init__(self):
        playing = True

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __str__(self):
        return f'{self.value} of {self.suit}'

class Player():
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.hand = []

class Deck():
    def __init__(self):
        # building deck of cards with nested for loop:
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

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

    # Is it time to break out of the main game loop?
    play_again = input("Would you like to play again? (y/n) ")

    if play_again == 'n':
        playing = False


# TODO:
# handling aces: if aces in hand and total over 21, subtract 10 times the number of aces.
