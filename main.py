"""Main script. User is 'P2'"""

import pygame
from pygame.locals import *
import setup
import winner
import trick
import hand

# 'depth_factor' means "how many tricks the minimax algorithm searches."
depth_factor = 1
 
# 'game' is a dictionary that stores important backend variables used throughout the program.   
game = setup.setup_game(depth_factor)

# Setup pygame.
pygame.init()
screen_size = (1250, 700)
screen = pygame.display.set_mode(screen_size)
background = pygame.transform.scale(pygame.image.load("images/background.jpeg").convert(), screen_size)

# Until the game has ended, continue looping (playing the game).
while not winner.has_won(game):
    # Until a particular hand is not finished, continue looping (playing tricks).
    while not game["hand_finished"]:
        trick.play_trick(game) 
    hand.setup_next_hand(game)

# Conclude game.
winner.declare_winner(game)