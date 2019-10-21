import time
from random import randint, choice

class Game():
    def __init__(self):
        self.playing = True

    def check_for_bust(self, player):
        if player.total > 21:
            print(f"{player.name} BUSTED! {player.total}")
            return True

    def compare_results(player1, player2):
        if player1.total == player2.total:
            return f"It's a tie: Your score is {player1.score} ; Dealer's score is {player2.score}"
        elif player1.total > player2.total:
            return f"You win! : Your score is {player1.score} ; Dealer's score is {player2.score}"
        elif player1.total < player2.total:
            return f"Dealer wins! : Your score is {player1.score} ; Dealer's score is {player2.score}"

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
        self.play = None
        self.busted = False

    def calc_score(self):
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

    def set_play(self, choice):
        if choice == 'hit':
            deck.deal_card(self)
            player.play = "Hit"
        elif choice == 'stay':
            player.play = "Stay"

# TODO: I think i've figured out how to implement extracting the display cards to a method, while having different display methods for the player and the dealer. Solution: Make dealer a subclass of player and override the basic display method with the method that hides the first card facedown.


    # def display_cards(self):
    #     if self.name == 'dealer':
    #         # Display dealer's second card onward:
    #         print('\n', f"{dealer.name}'s hand:", end=" ")
    #         print("? of ?,", end=' ')
    #         for card in dealer.hand[1:]:
    #             print(card, end='')
    #
    #     else:
    #         # Display player's cards and total:
    #         print('\n', f"{player.name}'s hand after dealing cards:", end=" ")
    #         for card in player.hand:
    #             print(card, end='')
    #
    #         print('\n', f"{player.name}'s total = {player.score()}")


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

################################################################################
# Main game loop
################################################################################

game = Game()

player_name = input("Please type your name ")

while game.playing:

    player = Player(name=player_name)
    dealer = Player(name='Dealer')

    # Instantiate deck and deal first two cards to dealer and player
    deck = Deck()

    deck.deal_card(player, 2)
    deck.deal_card(dealer, 2)


    # Show player's cards
    print(f"{player.name}'s hand after dealing cards: ", '\n')
    for card in player.hand:
        print(card)
    # display player's current total
    print(f"{player.name}'s total = {player.calc_score()}")

    # Show dealer's cards from secont card on:
    print(f"{dealer.name}'s hand:", '\n')
    print("? of ?,", end=' ')
    for card in dealer.hand[1:]:
        print(card)

    print('\n')
    #  calculate dealer's current total
    dealer.calc_score()

    time.sleep(1)




    # Loop through and allow player and dealer to hit or stay until one busts or both stay. Check for bust with each pass.

    # while player.play != 'Stay' and dealer.play != 'Stay':
    #     choice = input("Would you like to hit or stay? (Hit/Stay)")
    #     player.set_play(choice)
    #
    #     if dealer.total > 16:
    #         dealer.set_play('Stay')
    #     else:
    #         dealer.set_play('Hit')
    #
    #     if player.total > 21 or dealer.total > 21:
    #         break

    while True:
        # Player: hit or stay?
        choice = input("Would you like to hit or stay? (Hit/Stay) ")
        if choice == 'hit':
            deck.deal_card(player)
            player.calc_score()
        if player.total > 21:
            player.busted = True
            print("You BUSTED!!! ")
            break
        elif choice == 'stay':
            player.play = 'stay'
        else:
            print("Please select a valid play. ")
            continue

        time.sleep(1)

        # display player's hand and score:
        print(f"{player.name}'s hand after dealing cards:", '\n')
        for card in player.hand:
            print(card, '\n')
        # display player's current total
        print('\n', f"{player.name}'s total = {player.total}")

        # dealer: hit or stay?
        if dealer.total <= 16:
            print("Dealer hits.")
            deck.deal_card(dealer)
            dealer.calc_score()
            dealer.play = 'stay'
        if dealer.total > 21:
            dealer.busted = True
            print("Dealer BUSTED!!! ")
            break
        elif dealer.total > 16:
            dealer.play = 'stay'

        print(f"{dealer.name}'s hand:", '\n')
        print("? of ?,", end=' ')
        for card in dealer.hand[1:]:
            print(card, '\n')

        if dealer.play == 'stay' and player.play == 'stay':
            break

    if player.busted:
        print(f"You busted! Dealer wins! Your score is {player.total} ; Dealer's total is {dealer.total}")
    elif dealer.busted:
        print(f"You win! Dealer busted! Your total is {player.total} ; Dealer's total is {dealer.total}")
    elif player.total == dealer.total:
        print(f"It's a tie: Your total is {player.total} ; Dealer's total is {dealer.total}")
    elif player.total > dealer.total:
        print(f"You win! : Your total is {player.total} ; Dealer's total is {dealer.total}")
    elif player.total < dealer.total:
        print(f"Dealer wins! : Your total is {player.total} ; Dealer's total is {dealer.total}")

        # display player's final hand and final total:
        print(f"{player.name}'s final:", '\n')
        for card in player.hand:
            print(card, '\n')
        # display player's current total
        print('\n', f"{player.name}'s total = {player.total}")

        # display player's final hand and final total:
        print(f"{dealer.name}'s final hand:", '\n')
        for card in dealer.hand:
            print(card, '\n')
        # display dealer's current total
        print('\n', f"{dealer.name}'s total = {dealer.total}")



    # Is it time to break out of the main game loop?
    play_again = input("Would you like to play again? (y/n) ")

    if play_again == 'n':
        game.playing = False
        print("Thanks for playing!")
        time.sleep(2)
