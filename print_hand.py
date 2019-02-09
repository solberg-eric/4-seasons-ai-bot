def print_hand(player_one_cards_in_play, player_one_hand, player_one_trick_pile, player_two_cards_in_play, player_two_hand, player_two_trick_pile, trump): # From 2.2
    print_player_hand(player_two_hand, trump, "p2", player_two_trick_pile)
    print_player_cards_in_play(player_two_cards_in_play, "p2")
    print_player_cards_in_play(player_one_cards_in_play, "p1")
    print_player_hand(player_one_hand, trump, "p1", player_one_trick_pile)

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