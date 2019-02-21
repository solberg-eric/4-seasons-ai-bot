"""Play a trick."""

import sys
import time
import pygame
from pygame.locals import *
import display
import minimax
import evaluate
import card
import click

# From main
def play_trick(game):
    """Play a trick. Returns: none."""
    play_order = determine_play_order(game)

    # A trick.
    for i in range(2): # Loop twice for each trick because both players play twice per trick.
        # Each player play once.
        for player in play_order: # Loop twice. For each loop, one player plays once. Is ultimately looped four times (if you include the parent 'for' loop) because each player plays two times.
            display.blit_game(game)
            display.print_hand(game["p1"].cards_in_play, game["p1"].hand, game["p1"].trick_pile, game["p2"].cards_in_play, game["p2"].hand, game["p2"].trick_pile, game["trump_order"])
            if player == "p2":
                your_turn(game)
            else:
                computer_plays(game, minimax.get_best_play(game, i, player, play_order))
                # pygame.time.delay(1000) # not working at all.
                if play_order.index(player) == 0 and i == 0 or play_order.index(player) == 1 and i == 1:
                    game["turn"] = "p2c1"
                else:
                    game["turn"] = "p2c2"
            if play_order.index(player) == 0 and i == 0:
                game["lead_suit"] = game[game["lead_player"]].cards_in_play[0][1]
            print_test(game)

    setup_next_trick(game)

# From self.play_trick()
def determine_play_order(game):
    if game["lead_player"] == "p1":
        play_order = ["p1", "p2"]
    else:
        play_order = ["p2", "p1"]
    return play_order

# From self.play_trick()
def your_turn(game):
    """User's turn to play."""
    while game["user_has_played"] == False:
        for event in pygame.event.get(): # check to see if double clicking really fast creates bug and plays twice.

            # Enable user to close program
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            elif event.type == QUIT:
                sys.exit()

            # If mouse is clicked, potentially do something
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = x, y = pygame.mouse.get_pos()
                click.check_location_of_click(game, mouse_pos)

    game["user_has_played"] = False

# From self.play_trick()
def computer_plays(game, result):
    """Player 1 play a card."""
    card_index = game["p1"].hand.index(result[1])
    card.play_card(game, card_index, "p1")

# From self.play_trick() or minimax.if_trick_complete()
def setup_next_trick(game):
    """Prepare the game for the next trick."""
    players_list = ["p1", "p2"]
    if len(game["p1"].hand) == 0 or len(game["p2"].hand) == 0:
        game["hand_finished"] = True
    evaluate.determine_winner_of_trick(game)
    game["lead_player"] = game["player_winning_trick"]
    add_cards_to_trick_pile(game)
    for player in players_list:
        game[player].cards_in_play_ranks = [0, 0]
    print("***** " + game["player_winning_trick"] + " WINS TRICK ******")
    print("***** " + game["lead_player"] + " LEADS NEXT TRICK ******")
    print()

# From self.setup_next_trick()
def add_cards_to_trick_pile(game):
    for i in range(2):
        game[game["player_winning_trick"]].trick_pile.append(game["p1"].cards_in_play.pop())
        game[game["player_winning_trick"]].trick_pile.append(game["p2"].cards_in_play.pop())

# Only called for testing purposes
def print_test(game):
    print()
    print()
    print()
    print()
    print()
    print(game)
    print()
    print()
    print()
    print()
    print()


    