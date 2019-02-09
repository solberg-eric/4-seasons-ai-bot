import card

#4.4
def minimax(game): # From 3.3
    player = game["player_optimizing"]
    if check_if_someone_has_won_or_if_game_depth_is_zero(game):
        #print("WHATTT")
        return update_current_value(game) # values the game position
    best_value, best_play = update_pre_values(game, player)
    #print("Best Valuee: " + str(best_value))
    #print("Best Play: " + best_play)
    for play in game[player].hand:
        temp_game_status = deepcopy(game)
        card_index = temp_game_status[player].hand.index(play)
        card.play_card(temp_game_status, card_index, player)
        if_lead_play(temp_game_status) # then declare lead suit
        if_trick_complete(temp_game_status) # and have not reached deepest node, then setup next trick and possibly hand
        prepare_for_next_level_of_minimax_checking(temp_game_status, player) # changes optimizing player
        hypothetical_value = minimax(temp_game_status)[0]
        best_value, best_play = update_post_values(game, hypothetical_value, best_value, best_play, play, player)
        can_prune = prune_if_possible(game)
        if can_prune:
            break
    return [best_value, best_play]

def check_if_someone_has_won_or_if_game_depth_is_zero(game):
    if L2.has_won(game) or game["depth"] == 0: # To 2.1
        return True
    else:
        return False

def update_current_value(game):
    game["value"] += evaluate_game(game) # To 6.0
    return [game["value"], ""]

def update_pre_values(game, player):
    if player == "p1":
        return -float("Inf"), game[player].hand[0]
    else:
        return float("Inf"), game[player].hand[0]

def if_lead_play(temp_game_status):
    if temp_game_status["depth"] % 4 == 0:
        temp_game_status["lead_suit"] = temp_game_status[temp_game_status["lead_player"]].cards_in_play[0][1]

def if_trick_complete(temp_game_status):
    if (temp_game_status["depth"]-1) % 4 == 0 and (temp_game_status["depth"]-1) != 0:
        temp_game_status["value"] += evaluate_game(temp_game_status) # 6.0
        temp_game_status["p1"].cost = 0
        temp_game_status["p1"].gain = 0
        temp_game_status["p2"].cost = 0
        temp_game_status["p2"].gain = 0
        setup_next_trick(temp_game_status) # To 3.5
        if temp_game_status["hand_finished"]:
            setup_next_hand(temp_game_status) # To 2.3

def prepare_for_next_level_of_minimax_checking(temp_game_status, player):
    temp_game_status["depth"] -= 1
    if player == "p1":
        temp_game_status["player_optimizing"] = "p2"
    else:
        temp_game_status["player_optimizing"] = "p1"

def update_post_values(game, hypothetical_value, best_value, best_play, play, player):
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

def prune_if_possible(game):
    if game["alpha"] >= game["beta"]:
        return True
    else:
        return False