from models.player import Player

def rps(player1, player2):

    if player1.choice == player2.choice:
        return 'draw'
    if player1.choice.lower() == 'rock':
        if player2.choice() == 'scissors':
            return 'player 1 wins'
        if player2.choice.lower() == 'paper':
            return 'player 2 wins'

    if player1.choice.lower() == 'paper':
        if player2.choice.lower() == 'rock':
            return 'player 1 wins'
        if player2.choice.lower() == 'scissors':
            return 'player 2 wins'

    if player1.choice.lower() == 'scissors':
        if player2.choice.lower() == 'paper':
            return 'player 1 wins'
        if player2.choice.lower() == 'rock':
            return 'player 2 wins'