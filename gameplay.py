from copy import deepcopy
from evaluate import *
from print_hand import *

def lead_player():
    while True:
        response = input("Are you the starting player? (y/n): ")
        print()
        if response == "y":
            return "p1"
            break
        elif response == "n":
            return "p2"
            break

def has_won(game):
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

def declare_winner(game):
    if has_won(game):
        if game["p1"].has_won:
            print("Player One wins!")
        else:
            print("Player Two wins!")

def print_game_status(game):
    print()
    print("************ Game Status ************")
    print()
    print("p1 hand: " + str(game["p1"].hand))
    print("p1 cards in play: " + str(game["p1"].cards_in_play))
    print("p1 cards in play ranks: " + str(game["p1"].cards_in_play_ranks))
    print("p1 trick pile: " + str(game["p1"].trick_pile))
    print("p1 cost: " + str(game["p1"].cost))
    print("p1 gain: " + str(game["p1"].gain))
    print("p1 has won: " + str(game["p1"].has_won))
    print()
    print("p2 hand: " + str(game["p2"].hand))
    print("p2 cards in play: " + str(game["p2"].cards_in_play))
    print("p2 cards in play ranks: " + str(game["p2"].cards_in_play_ranks))
    print("p2 trick pile: " + str(game["p2"].trick_pile))
    print("p2 cost: " + str(game["p2"].cost))
    print("p2 gain: " + str(game["p2"].gain))
    print("p2 has won: " + str(game["p2"].has_won))
    print()
    print(game)
    print()
    print("*************************************")
    print()

def prune_if_possible(game):
    if game["alpha"] >= game["beta"]:
        return True
    else:
        return False

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

def prepare_for_next_level_of_minimax_checking(temp_game_status, player):
    temp_game_status["depth"] -= 1
    if player == "p1":
        temp_game_status["player_optimizing"] = "p2"
    else:
        temp_game_status["player_optimizing"] = "p1"

def if_trick_complete(temp_game_status):
    if (temp_game_status["depth"]-1) % 4 == 0 and (temp_game_status["depth"]-1) != 0:
        temp_game_status["value"] += evaluate_game(temp_game_status)
        temp_game_status["p1"].cost = 0
        temp_game_status["p1"].gain = 0
        temp_game_status["p2"].cost = 0
        temp_game_status["p2"].gain = 0
        setup_next_trick(temp_game_status)
        if temp_game_status["hand_finished"]:
            setup_next_hand(temp_game_status)

def if_lead_play(temp_game_status):
    if temp_game_status["depth"] % 4 == 0:
        temp_game_status["lead_suit"] = temp_game_status[temp_game_status["lead_player"]].cards_in_play[0][1]

def update_current_value(game):
    game["value"] += evaluate_game(game)
    return [game["value"], ""]

def update_pre_values(game, player):
    if player == "p1":
        return -float("Inf"), game[player].hand[0]
    else:
        return float("Inf"), game[player].hand[0]

def check_if_someone_has_won_or_if_game_depth_is_zero(game):
    if has_won(game) or game["depth"] == 0:
        return True
    else:
        return False

def minimax(game):
    player = game["player_optimizing"]
    if check_if_someone_has_won_or_if_game_depth_is_zero(game):
        #print("WHATTT")
        return update_current_value(game)#values the game position
    best_value, best_play = update_pre_values(game, player)
    #print("Best Valuee: " + str(best_value))
    #print("Best Play: " + best_play)
    for play in game[player].hand:
        temp_game_status = deepcopy(game)
        card_index = temp_game_status[player].hand.index(play)
        play_card(temp_game_status, card_index, player)
        if_lead_play(temp_game_status)#then declare lead suit
        if_trick_complete(temp_game_status) #and have not reached deepest node, then setup next trick and possibly hand
        prepare_for_next_level_of_minimax_checking(temp_game_status, player)#changes optimizing player
        hypothetical_value = minimax(temp_game_status)[0]
        best_value, best_play = update_post_values(game, hypothetical_value, best_value, best_play, play, player)
        can_prune = prune_if_possible(game)
        if can_prune:
            break
    return [best_value, best_play]

def arrange_cards_in_hand(game, player):
    temp_hand = []
    rank_list = ["A", "K", "Q", "J"]
    for i in range(4):
        for rank in rank_list:
            for card in game[player].hand:
                if rank in card and game["trump_order"][i][0] in card:
                    temp_hand.append(card)
    game[player].hand = deepcopy(temp_hand)

def setup_next_hand(game):
    players_list = ["p1", "p2"]
    game["trump_order"].append(game["trump_order"].pop(0))
    game["hand_finished"] = False
    for player in players_list:
        game[player].hand = game[player].trick_pile
        game[player].cards_in_play = []
        game[player].cards_in_play_ranks = [0, 0]
        game[player].trick_pile = []
        arrange_cards_in_hand(game, player)

def setup_next_trick(game):
    players_list = ["p1", "p2"]
    if len(game["p1"].hand) == 0 or len(game["p2"].hand) == 0:
        game["hand_finished"] = True
    #print_game_status(game)
    determine_winner_of_trick(game)
    game["lead_player"] = game["player_winning_trick"]
    #print_game_status(game)
    add_cards_to_trick_pile(game)
    for player in players_list:
        game[player].cards_in_play_ranks = [0, 0]
    print("***** " + game["player_winning_trick"] + " WINS TRICK ******")
    print()
    print("P1's trick pile: " + str(game["p1"].trick_pile))
    print("P2's trick pile: " + str(game["p2"].trick_pile))
    print()
    print("***** " + game["lead_player"] + " LEADS NEXT TRICK ******")
    print()

def opponent_plays(game): 
    while True:
        response = input("What card does P2 play? (enter as string): ")
        print()
        if response in game["p2"].hand:
            card_index = game["p2"].hand.index(response)
            play_card(game, card_index, "p2")
            break

def play_card(game, card_index, player):
    game[player].cards_in_play.append(game[player].hand.pop(card_index))

def player_plays(game, result):
    print("Best play: " + str(result[1]))
    print("Resulting value: " + str(result[0]))
    while True:
        response = input("Press ENTER to play the " + str(result[1]) + ": ")
        print()
        if response == "":
            card_index = game["p1"].hand.index(result[1])
            play_card(game, card_index, "p1")
            break;
    #print("P1 hand: " + str(game["p1"].hand))
    #print("P1 cards in play: " + str(game["p1"].cards_in_play))
    #print("P1 card ranks: " + str(game["p1"].cards_in_play_ranks))

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

def get_best_play(game, i, player, play_order):
    reset_values_for_minimax(game, i, player, play_order)
    ##print("Goin' into the minimax with following Game Status...")
    #print_game_status(game)
    result = minimax(game)
    print(result)
    return result

def determine_play_order(game):
    if game["lead_player"] == "p1":
        play_order = ["p1", "p2"]
    else:
        play_order = ["p2", "p1"]
    return play_order

def trick(game):
    play_order = determine_play_order(game)
    for i in range(2): #range(2) because each player plays twice per trick
        for player in play_order:   
            print_hand(game["p1"].cards_in_play, game["p1"].hand, game["p2"].cards_in_play, game["p2"].hand, game["trump_order"])
            if player == "p1":
                player_plays(game, get_best_play(game, i, player, play_order))
            else:
                opponent_plays(game)
            if play_order.index(player) == 0 and i == 0:
                game["lead_suit"] = game[game["lead_player"]].cards_in_play[0][1]
    setup_next_trick(game)
    #print_game_status(game)

def play_game(game):
    while not has_won(game):
        while not game["hand_finished"]:
            trick(game)
        setup_next_hand(game)

def setup_game(depth):
    class Player:
        def __init__(self, hand, cards_in_play, cards_in_play_ranks, trick_pile, cost, gain, has_won):
            self.hand = hand
            self.cards_in_play = cards_in_play
            self.cards_in_play_ranks = cards_in_play_ranks
            self.trick_pile = trick_pile
            self.cost = cost
            self.gain = gain
            self.has_won = has_won
    #p1 = Player(["AH", "KH", "QH", "JH", "AS", "KS", "QS", "JS", "AD", "KD", "QD", "JD", "AC", "KC", "QC", "JC"], [], [0, 0], [], 0, 0, False)
    #p2 = Player(["AH", "KH", "QH", "JH", "AS", "KS", "QS", "JS", "AD", "KD", "QD", "JD", "AC", "KC", "QC", "JC"], [], [0, 0], [], 0, 0, False)
    #p1 = Player(["AH", "KH", "AS", "KS", "AD", "KD", "AC", "KC"], [], [0, 0], [], 0, 0, False)
    #p2 = Player(["AH", "KH", "AS", "KS", "AD", "KD", "AC", "KC"], [], [0, 0], [], 0, 0, False)
    p1 = Player(["AH", "KH", "QH", "AS", "KS", "QS", "AD", "KD", "QD", "AC", "KC", "QC"], [], [0, 0], [], 0, 0, False)
    p2 = Player(["AH", "KH", "QH", "AS", "KS", "QS", "AD", "KD", "QD", "AC", "KC", "QC"], [], [0, 0], [], 0, 0, False)    
    game = {
        "p1" : p1,
        "p2" : p2,
        "depth" : depth,
        "alpha" : -float("Inf"),
        "beta" : float("Inf"),
        "trump_order" : ["Hearts", "Spades", "Diamonds", "Clubs"],
        "lead_player" : lead_player(), #returns either "p1" or "p2" depending on user input
        "lead_suit" : None, #"H", "S", "D", or "C"
        "player_winning_trick" : None, #eventually "p1" or "p2"
        "hand_finished" : False,
        "value" : 0,
        "player_optimizing" : "p1"
    }
    return game

def lets_play_four_seasons(depth):
    #depth *= 4
    game = setup_game(depth)
    play_game(game)
    declare_winner(game)