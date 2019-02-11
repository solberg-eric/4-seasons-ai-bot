"""Main script."""

import setup
import winner
import trick
import hand

# 'depth_factor' means "how many tricks the minimax algorithm searches."
depth_factor = 1
 
# 'game' is a dictionary that stores important values used throughout the program.   
game = setup.setup_game(depth_factor)

# Until the game has ended, continue looping (playing the game).
while not winner.has_won(game):
    # Until a particular hand is not finished, continue looping (playing tricks).
    while not game["hand_finished"]:
        trick.play_trick(game) 
    hand.setup_next_hand(game)

# Conclude game.
winner.declare_winner(game)