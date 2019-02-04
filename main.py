from gameflow import *

#0.0
def lets_play_four_seasons(depth):
    game = setup_game(depth) # To 1.0
    play_game(game) # To 1.1

# Uncomment lines 5 and 6 for whitespace buffer at start (used to easily locate the beginning of the program in the terminal).

#for i in range(10):
#        print()

# The argument value is the depth of the search (ie. n "tricks" deep).
lets_play_four_seasons(1)