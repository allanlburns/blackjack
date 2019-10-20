class Game():
    def __init__(self):
        playing = True

class Card():
    pass

class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.hand = []

class Deck():
    pass

playing = True

while playing:
    player_name = input("Please type your name ")

    player = Player(name=player_name)
    dealer = Player(name='Dealer')

    print(f'{dealer.name} has {dealer.hand}')
    print(f'{player.name} has {player.hand}')

    playing = False
