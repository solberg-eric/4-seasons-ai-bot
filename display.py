"""Updates pygame display."""

import pygame
from pygame.locals import *
import os

# Setup pygame.
pygame.init()
screen_size = (1250, 700)
screen = pygame.display.set_mode(screen_size)
background = pygame.transform.scale(pygame.image.load("images/background.jpeg").convert(), screen_size)
cards_in_play_rects = {
    "p2c1" : pygame.Rect((230, 360), (184, 250)),
    "p2c2" : pygame.Rect((255, 377), (184, 250)),
    "p1c1" : pygame.Rect((230, 90), (184, 250)),
    "p1c2" : pygame.Rect((205, 73), (184, 250))
}

# From setup.setup_game()
def create_hand(player_num): # pygame
    # Add cards to Player 1's or Player 2's hand
    hand = {}
    for filename in os.listdir("images"):
        path_to_image = "images/" + filename
        if filename.startswith(player_num):
            card = pygame.image.load(path_to_image).convert()
            card_name = filename[1:3]
            hand[card_name] = card
    return hand

# P2 (user) has cards labeled w/ #1
p2_images = create_hand("1")
# P1 (computer) has cards labeled w/ #2
p1_images = create_hand("2")

def blit_game(game):
    """Update display of entire game."""
    # Blit background
    screen.blit(background, (0,0))
    # Blit Player 2's (user) hand
    for i in range(len(game["p2"].hand)):
        screen.blit(p2_images[game["p2"].hand[i]], ((i+1)*27, 648))
    # Blit Player 1's (computer) hand
    for i in range(len(game["p1"].hand)-1, -1, -1):
        screen.blit(p1_images[game["p1"].hand[i]], (i*27+27, -198))
    # Blit Player 2's (user) cards_in_play:
    if len(game["p2"].cards_in_play) >= 1:
        screen.blit(p2_images[game["p2"].cards_in_play[0]], cards_in_play_rects["p2c1"])
    if len(game["p2"].cards_in_play) >= 2:
        screen.blit(p2_images[game["p2"].cards_in_play[1]], cards_in_play_rects["p2c2"])
    # Blit Player 1's (computer) cards_in_play:
    if len(game["p1"].cards_in_play) >= 1:
        screen.blit(p1_images[game["p1"].cards_in_play[0]], cards_in_play_rects["p1c1"])
    if len(game["p1"].cards_in_play) >= 2:
        screen.blit(p1_images[game["p1"].cards_in_play[1]], cards_in_play_rects["p1c2"])
    # Blit Player 2's (user) trick_pile:
#    for i in range(len(game["p2"].trick_pile)):
#        screen.blit(p2_images[game["p2"].trick_pile[i]], ((i+1)*27, 648))
    # Blit Player 1's (computer) trick_pile:
#    for i in range(len(game["p1"].hand)-1, -1, -1):
#        screen.blit(p1_images[game["p1"].trick_pile[i]], (i*27+27, -198))

    pygame.display.flip()




# From trick.play_trick()
def print_hand(player_one_cards_in_play, player_one_hand, player_one_trick_pile, player_two_cards_in_play, player_two_hand, player_two_trick_pile, trump):
    """Prints the current game-state to the console. Args used in print_player_hand and print_player_cards_in_play functions.
    
    Args:
        player_one_cards_in_play (list) of (strings): p1's cards in play.
        player_one_hand (list) of (strings): p1's cards in hand.
        player_one_trick_pile (list) of (strings): p1's cards in trick pile (unordered). Ex. ['JS', 'JC', 'AS', 'QC', 'KH', 'AH', 'JC', 'QS']

        player_two_cards_in_play (list) of (strings): p2's cards in play.
        player_two_hand (list) of (strings): p2's cards in hand.
        player_two_trick_pile (list) of (strings): p2's cards in trick pile (unordered). Ex. ['AH', 'QC', 'JH', 'KS']

        trump (list) of (strings): The trump order. Ex. ['Hearts', 'Spades', 'Diamonds', 'Clubs']

    Return:
        none
    """
    print_player_hand(player_two_hand, trump, "p2", player_two_trick_pile)
    print_player_cards_in_play(player_two_cards_in_play, "p2")
    print_player_cards_in_play(player_one_cards_in_play, "p1")
    print_player_hand(player_one_hand, trump, "p1", player_one_trick_pile)

# From self.print_hand()
def print_player_hand(hand_unsorted, trump, player, trick_pile):
    # i, j, k, l used as incrementing values.
    i = 0
    j = 0
    k = 0
    l = 0

    # template for printed hand
    hand_sorted = [["  ", "  ", "  ", "  "],
                   ["  ", "  ", "  ", "  "],
                   ["  ", "  ", "  ", "  "],
                   ["  ", "  ", "  ", "  "],
                   ["  ", "  ", "  ", "  "],
                   ["  ", "  ", "  ", "  "],
                   ["  ", "  ", "  ", "  "],
                   ["  ", "  ", "  ", "  "]]

    # Fills template with cards from player's hand.
    for card in hand_unsorted:
        if trump[0][0] in card:
            hand_sorted[i][0] = card
            i += 1
        elif trump[1][0] in card:
            hand_sorted[j][1] = card
            j += 1
        elif trump[2][0] in card:
            hand_sorted[k][2] = card
            k += 1
        else:
            hand_sorted[l][3] = card
            l += 1

    d = 8 # 'd' tracks how many lines should be printed in a player's hand
    # Deletes unused lines from hand_sorted so they do not print to console.
    for i in range(7, -1, -1):
        if hand_sorted[i][0] == "  " and hand_sorted[i][1] == "  " and hand_sorted[i][2] == "  " and hand_sorted[i][3] == "  ":
            hand_sorted.pop(i)
            d = i
        else:
            break
    if player == "p2":
        print("   P2 Hand   ")
        print("_____________   P2 Trick Pile: " + str(trick_pile))
    for i in range(d):
        print(" " + hand_sorted[i][0] + " " + hand_sorted[i][1] + " " + hand_sorted[i][2] + " " + hand_sorted[i][3])
    if player == "p1":
        print("_____________   P1 Trick Pile: " + str(trick_pile))
        print("   P1 Hand   ")
    print()

# From self.print_hand()
def print_player_cards_in_play(cards_in_play, player):
    if player == "p2":
        if len(cards_in_play) == 2:
            print("  2. " + cards_in_play[1])
            print("  1. " + cards_in_play[0])
            print()
        elif len(cards_in_play) == 1:
            print("  2. ")
            print("  1. " + cards_in_play[0])
            print()        
        else:
            print("  2. ")
            print("  1. ")
            print()  
    else:
        if len(cards_in_play) == 2:
            print("  1. " + cards_in_play[0])
            print("  2. " + cards_in_play[1])
            print()
        elif len(cards_in_play) == 1:
            print("  1. " + cards_in_play[0])
            print("  2. ")
            print()        
        else:
            print("  1. ")
            print("  2. ")
            print() 

# Function below only used for testing purposes.

#def print_game_status(game):
#    print()
#    print("************ Game Status ************")
#    print()
#    print("p1 hand: " + str(game["p1"].hand))
#    print("p1 cards in play: " + str(game["p1"].cards_in_play))
#    print("p1 cards in play ranks: " + str(game["p1"].cards_in_play_ranks))
#    print("p1 trick pile: " + str(game["p1"].trick_pile))
#    print("p1 cost: " + str(game["p1"].cost))
#    print("p1 gain: " + str(game["p1"].gain))
#    print("p1 has won: " + str(game["p1"].has_won))
#    print()
#    print("p2 hand: " + str(game["p2"].hand))
#    print("p2 cards in play: " + str(game["p2"].cards_in_play))
#    print("p2 cards in play ranks: " + str(game["p2"].cards_in_play_ranks))
#    print("p2 trick pile: " + str(game["p2"].trick_pile))
#    print("p2 cost: " + str(game["p2"].cost))
#    print("p2 gain: " + str(game["p2"].gain))
#    print("p2 has won: " + str(game["p2"].has_won))
#    print()
#    print(game)
#    print()
#    print("*************************************")
#    print()
