#7.0
def determine_gain(game): # From 6.0
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
    #print(game["player_winning_trick"] + " gains: " + str(game[game["player_winning_trick"]].gain))

#7.1
def determine_cost(game): # From 6.0
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
        #print(player + " costs: " + str(game[player].cost))
    #print()

#7.2
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

#7.3
def temp(game):
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
