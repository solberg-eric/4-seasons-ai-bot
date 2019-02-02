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




def add_cards_to_trick_pile(game):
    for i in range(2):
        game[game["player_winning_trick"]].trick_pile.append(game["p1"].cards_in_play.pop())
        game[game["player_winning_trick"]].trick_pile.append(game["p2"].cards_in_play.pop())

def determine_cost(game):
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

def determine_gain(game):
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

def set_card_ranks(game):
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

def determine_winner_of_trick(game):
    set_card_ranks(game)#set ranks of cards in play
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

def evaluate_game(game):
    determine_winner_of_trick(game)
    #print(game["player_winning_trick"])
    determine_gain(game)
    determine_cost(game)
    return (game["p1"].gain - game["p1"].cost) - (game["p2"].gain - game["p2"].cost)