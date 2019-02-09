"""Main"""

import setup
import winner
import trick
import hand

depth = 1
    
game = setup.setup_game(depth)

while not winner.has_won(game):
    while not game["hand_finished"]:
        trick.play_trick(game)
    hand.setup_next_hand(game)

winner.declare_winner(game)