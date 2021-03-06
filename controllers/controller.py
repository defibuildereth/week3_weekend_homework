from flask import render_template
from app import app
# from models.player_list import rps
from models.player import Player
from models.game import Game

@app.route('/<player1_choice>/<player2_choice>')
def index(player1_choice, player2_choice):
    player1 = Player('Player 1', player1_choice)
    player2 = Player('Player 2', player2_choice)
    winner = Game.result(player1, player2)
    loser = Game.loser(player1, player2)
    return render_template('base.html', winner = winner, loser = loser)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')