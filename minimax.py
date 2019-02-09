from copy import deepcopy
import card
import winner
import evaluate
import trick
import hand

# From trick.play_trick()
def get_best_play(game, i, player, play_order):
    reset_values_for_minimax(game, i, player, play_order)
    result = minimax(game)
    return result

# From self.get_best_play()
def reset_values_for_minimax(game, i, player, play_order):
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

# From self.get_best_play()
def minimax(game):
    player = game["player_optimizing"]
    if check_if_someone_has_won_or_if_game_depth_is_zero(game):
        return update_current_value(game) # values the game position
    best_value, best_play = update_pre_values(game, player)
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

# From self.minimax()
def check_if_someone_has_won_or_if_game_depth_is_zero(game):
    if winner.has_won(game) or game["depth"] == 0:
        return True
    else:
        return False

# From self.minimax()
def update_current_value(game):
    game["value"] += evaluate.evaluate_game(game)
    return [game["value"], ""]

# From self.minimax()
def update_pre_values(game, player):
    if player == "p1":
        return -float("Inf"), game[player].hand[0]
    else:
        return float("Inf"), game[player].hand[0]

# From self.minimax()
def if_lead_play(temp_game_status):
    if temp_game_status["depth"] % 4 == 0:
        temp_game_status["lead_suit"] = temp_game_status[temp_game_status["lead_player"]].cards_in_play[0][1]

# From self.minimax()
def if_trick_complete(temp_game_status):
    if (temp_game_status["depth"]-1) % 4 == 0 and (temp_game_status["depth"]-1) != 0:
        temp_game_status["value"] += evaluate.evaluate_game(temp_game_status)
        temp_game_status["p1"].cost = 0
        temp_game_status["p1"].gain = 0
        temp_game_status["p2"].cost = 0
        temp_game_status["p2"].gain = 0
        trick.setup_next_trick(temp_game_status)
        if temp_game_status["hand_finished"]:
            hand.setup_next_hand(temp_game_status)

# From self.minimax()
def prepare_for_next_level_of_minimax_checking(temp_game_status, player):
    temp_game_status["depth"] -= 1
    if player == "p1":
        temp_game_status["player_optimizing"] = "p2"
    else:
        temp_game_status["player_optimizing"] = "p1"

# From self.minimax()
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

# From self.minimax()
def prune_if_possible(game):
    if game["alpha"] >= game["beta"]:
        return True
    else:
        return False