"""Evaluates potential game states from minimax algorithm"""

import trick

# From minimax.update_current_value() or minimax.if_trick_complete()
def evaluate_game(game):
    determine_winner_of_trick(game)
    determine_gain(game)
    determine_cost(game)
    return (game["p1"].gain - game["p1"].cost) - (game["p2"].gain - game["p2"].cost)

# From trick.setup_next_trick() or self.evaluate_game()
def determine_winner_of_trick(game):
    set_card_ranks(game) # Set ranks of cards in play
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
    if game["player_winning_trick"] == "p1":
        game["turn"] = "p1c1"
    else:
        game["turn"] = "p2c2"

# From self.determine_winner_of_trick()
def set_card_ranks(game):
    """Set the ranks of the cards (to determine which cards beat which cards during the trick)"""
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

# From self.evaluate_game()
def determine_gain(game):
    """Determine the benefit of the game state for the player"""
    players_list = ["p1", "p2"]
    for player in players_list:
        for card in game[player].cards_in_play:
            if "A" in card:
                game[game["player_winning_trick"]].gain += 4
            elif "K" in card:
                game[game["player_winning_trick"]].gain += 3
            elif "Q" in card:
                game[game["player_winning_trick"]].gain += 2
            else:
                game[game["player_winning_trick"]].gain += 1
            if game["trump_order"][1][0] in card:
                game[game["player_winning_trick"]].gain += 6
            elif game["trump_order"][2][0] in card:
                game[game["player_winning_trick"]].gain += 4
            elif game["trump_order"][3][0] in card:
                game[game["player_winning_trick"]].gain += 2
            else:
                game[game["player_winning_trick"]].gain += 0

# From self.evaluate_game()
def determine_cost(game):
    """Determine the cost of the state for the player"""
    players_list = ["p1", "p2"]
    for player in players_list:
        for card in game[player].cards_in_play:
            if "A" in card:
                game[player].cost += 4
            elif "K" in card:
                game[player].cost += 3
            elif "Q" in card:
                game[player].cost += 2
            else:
                game[player].cost += 1
            if game["trump_order"][0][0] in card:
                game[player].cost += 6
            elif game["trump_order"][1][0] in card:
                game[player].cost += 4
            elif game["trump_order"][2][0] in card:
                game[player].cost += 2
            else:
                game[player].cost += 0
