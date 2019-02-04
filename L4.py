from copy import deepcopy
from L5 import *

#4.0
def print_player_hand(hand_unsorted, trump, player, trick_pile): # From 3.1
    i = 0
    j = 0
    k = 0
    l = 0
    hand_sorted = [["  ", "  ", "  ", "  "],
                   ["  ", "  ", "  ", "  "],
                   ["  ", "  ", "  ", "  "],
                   ["  ", "  ", "  ", "  "],
                   ["  ", "  ", "  ", "  "],
                   ["  ", "  ", "  ", "  "],
                   ["  ", "  ", "  ", "  "],
                   ["  ", "  ", "  ", "  "]]
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
    d = 8
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

#4.1
def print_player_cards_in_play(cards_in_play, player): # From 3.1
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

#4.2
def play_card(game, card_index, player): # From 3.2, 3.4
    game[player].cards_in_play.append(game[player].hand.pop(card_index))

#4.3
def reset_values_for_minimax(game, i, player, play_order): # From 3.3
    if i == 0 and play_order.index(player) == 0:
        game["depth"] = 4
    elif i == 0 and play_order.index(player) == 1:
        game["depth"] = 3
    elif i == 1 and play_order.index(player) == 0:
        game["depth"] = 2
    elif i == 1 and play_order.index(player) == 1:
        game["depth"] = 1
    else:
        print("ERROR")
    game["alpha"] = -float("Inf")
    game["beta"] = float("Inf")
    game["player_optimizing"] : "p1"

#4.4
def minimax(game): # From 3.3
    player = game["player_optimizing"]
    if check_if_someone_has_won_or_if_game_depth_is_zero(game): # To 5.0
        #print("WHATTT")
        return update_current_value(game) # To 5.1 #values the game position
    best_value, best_play = update_pre_values(game, player) # To 5.2
    #print("Best Valuee: " + str(best_value))
    #print("Best Play: " + best_play)
    for play in game[player].hand:
        temp_game_status = deepcopy(game)
        card_index = temp_game_status[player].hand.index(play)
        play_card(temp_game_status, card_index, player) # To 4.2
        if_lead_play(temp_game_status) # To 5.3 #then declare lead suit
        if_trick_complete(temp_game_status) # To 5.4 #and have not reached deepest node, then setup next trick and possibly hand
        prepare_for_next_level_of_minimax_checking(temp_game_status, player) # To 5.5 #changes optimizing player
        hypothetical_value = minimax(temp_game_status)[0] # To self
        best_value, best_play = update_post_values(game, hypothetical_value, best_value, best_play, play, player) # To 5.6
        can_prune = prune_if_possible(game) # To 5.7
        if can_prune:
            break
    return [best_value, best_play]

# From setup_next_trick()
#   - determine_winner_of_trick()
#   - add_cards_to_trick_pile()

#4.5
def determine_winner_of_trick(game): # From 3.5, 6.0
    set_card_ranks(game) # To 5.8 #set ranks of cards in play
    second_player = "p2"
    if game["lead_player"] == "p2":
        second_player = "p1"
    game["player_winning_trick"] = game["lead_player"]
    winning_card_value = game[game["lead_player"]].cards_in_play_ranks[0]
    if (game[second_player].cards_in_play_ranks[0] > winning_card_value):
        game["player_winning_trick"] = second_player
        winning_card_value = game[second_player].cards_in_play_ranks[0]
    if (game[game["lead_player"]].cards_in_play_ranks[1] > winning_card_value):
        game["player_winning_trick"] = game["lead_player"]
        winning_card_value = game[game["lead_player"]].cards_in_play_ranks[1]
    if (game[second_player].cards_in_play_ranks[1] > winning_card_value):
        game["player_winning_trick"] = second_player
        winning_card_value = game[second_player].cards_in_play_ranks[1]

#4.6
def add_cards_to_trick_pile(game): # From 3.5
    for i in range(2):
        game[game["player_winning_trick"]].trick_pile.append(game["p1"].cards_in_play.pop())
        game[game["player_winning_trick"]].trick_pile.append(game["p2"].cards_in_play.pop())
