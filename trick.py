"""Play a trick"""

import print_hand

def play_trick(game): # From 1.1
    play_order = determine_play_order(game) # To 3.0
    for i in range(2): #range(2) because each player plays twice per trick
        for player in play_order:   
            print_hand.print_hand(game["p1"].cards_in_play, game["p1"].hand, game["p1"].trick_pile, game["p2"].cards_in_play, game["p2"].hand, game["p2"].trick_pile, game["trump_order"]) # To 3.1
            if player == "p1":
                player_plays(game, get_best_play(game, i, player, play_order)) # To 3.2, 3.3
            else:
                opponent_plays(game) # To 3.4
            if play_order.index(player) == 0 and i == 0:
                game["lead_suit"] = game[game["lead_player"]].cards_in_play[0][1]
    setup_next_trick(game) # To 3.5
    #print_game_status(game)

def determine_play_order(game): # From 2.2
    if game["lead_player"] == "p1":
        play_order = ["p1", "p2"]
    else:
        play_order = ["p2", "p1"]
    return play_order

def get_best_play(game, i, player, play_order): # From 2.2
    reset_values_for_minimax(game, i, player, play_order) # To 4.3
    ##print("Goin' into the minimax with following Game Status...")
    #print_game_status(game)
    result = minimax(game) # To 4.4
    return result

def player_plays(game, result): # From 2.2
    print("Best play: " + str(result[1]))
    print("Resulting value: " + str(result[0]))
    while True:
        response = input("Press ENTER to play the " + str(result[1]) + ": ")
        print()
        if response == "":
            card_index = game["p1"].hand.index(result[1])
            play_card(game, card_index, "p1") # To 4.2
            break;
    #print("P1 hand: " + str(game["p1"].hand))
    #print("P1 cards in play: " + str(game["p1"].cards_in_play))
    #print("P1 card ranks: " + str(game["p1"].cards_in_play_ranks))

def opponent_plays(game):  # From 2.2
    while True:
        response = input("What card does P2 play? (enter as string): ")
        print()
        if response in game["p2"].hand:
            card_index = game["p2"].hand.index(response)
            play_card(game, card_index, "p2") # To 4.2
            break

def setup_next_trick(game): # From 2.2, 5.4
    players_list = ["p1", "p2"]
    if len(game["p1"].hand) == 0 or len(game["p2"].hand) == 0:
        game["hand_finished"] = True
    #print_game_status(game)
    determine_winner_of_trick(game) # To 4.5
    game["lead_player"] = game["player_winning_trick"]
    #print_game_status(game)
    add_cards_to_trick_pile(game) # To 4.6
    for player in players_list:
        game[player].cards_in_play_ranks = [0, 0]
    print("***** " + game["player_winning_trick"] + " WINS TRICK ******")
    print("***** " + game["lead_player"] + " LEADS NEXT TRICK ******")
    print()
    