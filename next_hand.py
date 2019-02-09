#2.3
def setup_next_hand(game): # From 1.1, 5.4
    players_list = ["p1", "p2"]
    game["trump_order"].append(game["trump_order"].pop(0))
    game["hand_finished"] = False
    for player in players_list:
        game[player].hand = game[player].trick_pile
        game[player].cards_in_play = []
        game[player].cards_in_play_ranks = [0, 0]
        game[player].trick_pile = []
        arrange_cards_in_hand(game, player) # To 3.6