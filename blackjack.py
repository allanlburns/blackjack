import time
from random import randint, choice

class Game():
    def __init__(self):
        self.playing = True

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

    def score(self):
        for card in self.hand:
            if card.value == 'A' and self.hand.count('A') < 1:
                self.total += 11
            elif card.value in ['J', 'Q', 'K']:
                self.total += 10
            elif card.value == 'A' and total > 10:
                self.total += 1
            else:
                self.total += int(card.value)
        return self.total

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
            player.hand.append(self.cards.pop(randint(0, len(self.cards) - 1)))

game = Game()

player_name = input("Please type your name ")

while game.playing:

    player = Player(name=player_name)
    dealer = Player(name='Dealer')

    # Display dealer's and player's cards:

    # Placeholder for actual game logic
    print("Pretend we played a game...", '\n')
    deck = Deck()


    deck.deal_card(player, 2)
    deck.deal_card(dealer, 2)

    print('\n', f"{player.name}'s hand after dealing cards:", end=" ")
    for card in player.hand:
        print(card, end='')

    # display player's current total
    print('\n', f"{player.name}'s total = {player.score()}")

    print('\n', f"{dealer.name}'s hand:", end=" ")
    print("? of ?,", end=' ')
    for card in dealer.hand[1:]:
        print(card, end='')

    # display dealer's current total
    print('\n', f"Dealer's total = {dealer.score()}")


    # Is it time to break out of the main game loop?
    play_again = input("Would you like to play again? (y/n) ")

    if play_again == 'n':
        game.playing = False
        print("Thanks for playing!")
        time.sleep(2)


# TODO:
# handling aces: if aces in hand and total over 21, subtract 10 times the number of aces.
