from copy import deepcopy
from L3 import *

#2.0
def lead_player(): # From 1.0
    while True:
        response = input("Are you the starting player? (y/n): ")
        print()
        if response == "y":
            return "p1"
            break
        elif response == "n":
            return "p2"
            break

#2.1
def has_won(game):  # From 1.1, 1.2, 5.0
    if len(game["p1"].hand) == 0:
        game["p1"].has_won = False
        game["p2"].has_won = True
        return True
    elif len(game["p2"].hand) == 0 and len(game["p2"].cards_in_play) == 0:
        game["p1"].has_won = True
        game["p2"].has_won = False
        return True
    else:
        return False

#2.2
def trick(game): # From 1.1
    play_order = determine_play_order(game) # To 3.0
    for i in range(2): #range(2) because each player plays twice per trick
        for player in play_order:   
            print_hand(game["p1"].cards_in_play, game["p1"].hand, game["p2"].cards_in_play, game["p2"].hand, game["trump_order"]) # To 3.1
            if player == "p1":
                player_plays(game, get_best_play(game, i, player, play_order)) # To 3.2, 3.3
            else:
                opponent_plays(game) # To 3.4
            if play_order.index(player) == 0 and i == 0:
                game["lead_suit"] = game[game["lead_player"]].cards_in_play[0][1]
    setup_next_trick(game) # To 3.5
    #print_game_status(game)

#2.3
def setup_next_hand(game): # From 1.1, 5.4
    players_list = ["p1", "p2"]
    game["trump_order"].append(game["trump_order"].pop(0))
    game["hand_finished"] = False
    for player in players_list:
        game[player].hand = game[player].trick_pile
        game[player].cards_in_play = []
        game[player].cards_in_play_ranks = [0, 0]
        game[player].trick_pile = []
        arrange_cards_in_hand(game, player) # To 3.6
