"""Main"""

import setup
import trick
from next_hand
from gameflow import *

def lets_play_four_seasons(depth):
    game = setup.setup_game(depth)
    play_game(game)

def play_game(game):
    while not has_won(game): # To 2.1
        while not game["hand_finished"]:
            trick.play_trick(game)
        next_hand.setup_next_hand(game) # To 2.3
    declare_winner(game) # To 2.4

lets_play_four_seasons(1)