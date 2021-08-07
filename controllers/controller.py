from flask import render_template
from app import app
from models.player_list import rps

@app.route('/<player1_choice>/<player2_choice>')
def index(player1_choice, player2_choice):
    choices = [player1_choice, player2_choice]
    result = rps(choices)
    return render_template('base.html', result = result)