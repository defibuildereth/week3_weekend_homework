from models.player import Player
import pdb

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def result(player1, player2):
        # pdb.set_trace()
        if player1.choice.lower() == player2.choice.lower():
            return None
        elif player1.choice.lower() == 'rock':
            if player2.choice.lower() == 'scissors':
                return player1
            if player2.choice.lower() == 'paper':
                return player2

        elif player1.choice.lower() == 'paper':
            if player2.choice.lower() == 'rock':
                return player1
            if player2.choice.lower() == 'scissors':
                return player2

        elif player1.choice.lower() == 'scissors':
            if player2.choice.lower() == 'paper':
                return player1
            if player2.choice.lower() == 'rock':
                return player2

    def loser(player1, player2):
        players = [player1, player2]
        if Game.result(player1, player2):
            players.remove(Game.result(player1, player2))
            return players[0]

