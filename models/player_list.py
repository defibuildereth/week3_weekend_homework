# from models.player import Player

# player_1 = Player('Donald', 'rock')
# player_2 = Player('Finlay', 'paper')
# player_3 = Player('Michelle', 'scissors')

def rps(choices):

    if choices[0] == choices[1]:
        return 'draw'
    if choices[0].lower() == 'rock':
        if choices[1].lower() == 'scissors':
            return 'player 1 wins'
        if choices[1].lower() == 'paper':
            return 'player 2 wins'

    if choices[0].lower() == 'paper':
        if choices[1].lower() == 'rock':
            return 'player 1 wins'
        if choices[1].lower() == 'scissors':
            return 'player 2 wins'

    if choices[0].lower() == 'scissors':
        if choices[1].lower() == 'paper':
            return 'player 1 wins'
        if choices[1].lower() == 'rock':
            return 'player 2 wins'