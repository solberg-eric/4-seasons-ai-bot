from copy import deepcopy

# From main, minimax.if_trick_complete()
def setup_next_hand(game):
    players_list = ["p1", "p2"]
    game["trump_order"].append(game["trump_order"].pop(0))
    game["hand_finished"] = False
    for player in players_list:
        game[player].hand = game[player].trick_pile
        game[player].cards_in_play = []
        game[player].cards_in_play_ranks = [0, 0]
        game[player].trick_pile = []
        arrange_cards_for_next_hand(game, player)

# From self.setup_next_hand()
def arrange_cards_for_next_hand(game, player):
    temp_hand = []
    rank_list = ["A", "K", "Q", "J"]
    for i in range(4):
        for rank in rank_list:
            for card in game[player].hand:
                if rank in card and game["trump_order"][i][0] in card:
                    temp_hand.append(card)
    game[player].hand = deepcopy(temp_hand)