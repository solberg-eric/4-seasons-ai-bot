def print_hand(hand_unsorted, trump):
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
        if trump[0] in card:
            hand_sorted[i][0] = card
            i += 1
        elif trump[1] in card:
            hand_sorted[j][1] = card
            j += 1
        elif trump[2] in card:
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
    return hand_sorted, d

hand_unsorted = ["AH", "AH", "KH", "KH", "QH", "JD", "AC", "AC", "KC", "KC", "QC", "QC", "JC", "JC"]
trump = "HSDC"
hand, d = print_hand(hand_unsorted, trump)
print()
for i in range(d):
    print(" " + hand[i][0] + " " + hand[i][1] + " " + hand[i][2] + " " + hand[i][3])
print("*****************")