import time

class Game():
    def __init__(self):
        playing = True

class Card():
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Player():
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.hand = []

class Deck():
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']

playing = True

while playing:
    player_name = input("Please type your name ")

    player = Player(name=player_name)
    dealer = Player(name='Dealer')

    print('\n')
    print(f'{dealer.name} has {dealer.hand}')
    print(f'{player.name} has {player.hand}', '\n')

    time.sleep(1)

    print("Pretend we played a game...", '\n')

    play_again = input("Would you like to play again? (y/n) ")

    if play_again == 'n':
        playing = False

# handling aces: if aces in hand and total over 21, subtract 10 times the number of aces.
