import L2
from L3 import *
from L4 import *
from L6 import *

#5.0
def check_if_someone_has_won_or_if_game_depth_is_zero(game): # From 4.4
    if L2.has_won(game) or game["depth"] == 0: # To 2.1
        return True
    else:
        return False

#5.1
def update_current_value(game): # From 4.4
    game["value"] += evaluate_game(game) # To 6.0
    return [game["value"], ""]

#5.2
def update_pre_values(game, player): # From 4.4
    if player == "p1":
        return -float("Inf"), game[player].hand[0]
    else:
        return float("Inf"), game[player].hand[0]

#5.3
def if_lead_play(temp_game_status): # From 4.4
    if temp_game_status["depth"] % 4 == 0:
        temp_game_status["lead_suit"] = temp_game_status[temp_game_status["lead_player"]].cards_in_play[0][1]

#5.4
def if_trick_complete(temp_game_status): # From 4.4
    if (temp_game_status["depth"]-1) % 4 == 0 and (temp_game_status["depth"]-1) != 0:
        temp_game_status["value"] += evaluate_game(temp_game_status) # 6.0
        temp_game_status["p1"].cost = 0
        temp_game_status["p1"].gain = 0
        temp_game_status["p2"].cost = 0
        temp_game_status["p2"].gain = 0
        setup_next_trick(temp_game_status) # To 3.5
        if temp_game_status["hand_finished"]:
            setup_next_hand(temp_game_status) # To 2.3

#5.5
def prepare_for_next_level_of_minimax_checking(temp_game_status, player): # From 4.4
    temp_game_status["depth"] -= 1
    if player == "p1":
        temp_game_status["player_optimizing"] = "p2"
    else:
        temp_game_status["player_optimizing"] = "p1"

#5.6
def update_post_values(game, hypothetical_value, best_value, best_play, play, player): # From 4.4
    if player == "p1":
        if hypothetical_value > best_value:
            best_value = hypothetical_value
            best_play = play
        game["alpha"] = max(game["alpha"], best_value)
    else:
        if hypothetical_value < best_value:
            best_value = hypothetical_value
            best_play = play
        game["beta"] = min(game["beta"], best_value)
    return best_value, best_play

#5.7
def prune_if_possible(game): # From 4.4
    if game["alpha"] >= game["beta"]:
        return True
    else:
        return False

#5.8
def set_card_ranks(game):  # From 4.5
    players_list = ["p1", "p2"]
    for player in players_list:
        for card in game[player].cards_in_play:
            if game["lead_suit"] in card:
                if "A" in card:
                    game[player].cards_in_play_ranks[game[player].cards_in_play.index(card)] = 4 
                elif "K" in card:
                    game[player].cards_in_play_ranks[game[player].cards_in_play.index(card)] = 3
                elif "Q" in card:
                    game[player].cards_in_play_ranks[game[player].cards_in_play.index(card)] = 2
                else:
                    game[player].cards_in_play_ranks[game[player].cards_in_play.index(card)] = 1
            if game["trump_order"][0][0] in card:
                if "A" in card:
                    game[player].cards_in_play_ranks[game[player].cards_in_play.index(card)] = 8
                elif "K" in card:
                    game[player].cards_in_play_ranks[game[player].cards_in_play.index(card)] = 7
                elif "Q" in card:
                    game[player].cards_in_play_ranks[game[player].cards_in_play.index(card)] = 6
                else:
                    game[player].cards_in_play_ranks[game[player].cards_in_play.index(card)] = 5
        #print(game[player].cards_in_play)
        #print(game[player].cards_in_play_ranks)