from L4 import *

#3.0
def determine_play_order(game): # From 2.2
    if game["lead_player"] == "p1":
        play_order = ["p1", "p2"]
    else:
        play_order = ["p2", "p1"]
    return play_order

#3.1
def print_hand(player_one_cards_in_play, player_one_hand, player_two_cards_in_play, player_two_hand, trump): # From 2.2
    print_player_hand(player_two_hand, trump, "p2") # To 4.0
    print_player_cards_in_play(player_two_cards_in_play, "p2") # To 4.1
    print_player_cards_in_play(player_one_cards_in_play, "p1") # To 4.1
    print_player_hand(player_one_hand, trump, "p1") # To 4.0
    # Testing values below.

    #fix order of p2 cards in play
    #player_one_hand = ["AH", "AH", "KH", "QH", "KS", "QS", "JS", "JD", "AC", "AC", "KC", "KC"]
    #player_two_hand = ["AH", "AH", "KH", "KH", "QH", "JD", "AC", "AC", "KC", "QC", "QC", "JC"]
    #player_one_cards_in_play = ["QH", "JD"]
    #player_two_cards_in_play = ["QH", "JD"]
    #trump = ["Hearts", "Spades", "Diamonds", "Clubs"]
    #print()
    #print_hand(player_one_cards_in_play, player_one_hand, player_two_cards_in_play, player_two_hand, trump)
    #print()

#3.2
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

#3.3
def get_best_play(game, i, player, play_order): # From 2.2
    reset_values_for_minimax(game, i, player, play_order) # To 4.3
    ##print("Goin' into the minimax with following Game Status...")
    #print_game_status(game)
    result = minimax(game) # To 4.4
    print(result)
    return result

#3.4
def opponent_plays(game):  # From 2.2
    while True:
        response = input("What card does P2 play? (enter as string): ")
        print()
        if response in game["p2"].hand:
            card_index = game["p2"].hand.index(response)
            play_card(game, card_index, "p2") # To 4.2
            break

#3.5
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
    print()
    print("P1's trick pile: " + str(game["p1"].trick_pile))
    print("P2's trick pile: " + str(game["p2"].trick_pile))
    print()
    print("***** " + game["lead_player"] + " LEADS NEXT TRICK ******")
    print()

#3.6
def arrange_cards_in_hand(game, player): # From 2.3
    temp_hand = []
    rank_list = ["A", "K", "Q", "J"]
    for i in range(4):
        for rank in rank_list:
            for card in game[player].hand:
                if rank in card and game["trump_order"][i][0] in card:
                    temp_hand.append(card)
    game[player].hand = deepcopy(temp_hand)