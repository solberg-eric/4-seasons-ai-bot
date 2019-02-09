# From trick.play_trick()
def print_hand(player_one_cards_in_play, player_one_hand, player_one_trick_pile, player_two_cards_in_play, player_two_hand, player_two_trick_pile, trump):
    print_player_hand(player_two_hand, trump, "p2", player_two_trick_pile)
    print_player_cards_in_play(player_two_cards_in_play, "p2")
    print_player_cards_in_play(player_one_cards_in_play, "p1")
    print_player_hand(player_one_hand, trump, "p1", player_one_trick_pile)

# From self.print_hand()
def print_player_hand(hand_unsorted, trump, player, trick_pile):
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

# From self.print_hand()
def print_player_cards_in_play(cards_in_play, player):
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

# Only used when testing game state.
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