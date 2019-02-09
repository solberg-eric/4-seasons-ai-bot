"""Play a trick"""

import display
import minimax
import evaluate
import card

# From main
def play_trick(game):
    play_order = determine_play_order(game)
    for i in range(2): # range(2) because each player plays twice per trick
        for player in play_order:   
            display.print_hand(game["p1"].cards_in_play, game["p1"].hand, game["p1"].trick_pile, game["p2"].cards_in_play, game["p2"].hand, game["p2"].trick_pile, game["trump_order"])
            if player == "p1":
                player_plays(game, minimax.get_best_play(game, i, player, play_order))
            else:
                opponent_plays(game)
            if play_order.index(player) == 0 and i == 0:
                game["lead_suit"] = game[game["lead_player"]].cards_in_play[0][1]
    setup_next_trick(game)

# From self.play_trick()
def determine_play_order(game):
    if game["lead_player"] == "p1":
        play_order = ["p1", "p2"]
    else:
        play_order = ["p2", "p1"]
    return play_order

# From self.play_trick()
def player_plays(game, result):
    print("Best play: " + str(result[1]))
    print("Resulting value: " + str(result[0]))
    while True:
        response = input("Press ENTER to play the " + str(result[1]) + ": ")
        print()
        if response == "":
            card_index = game["p1"].hand.index(result[1])
            card.play_card(game, card_index, "p1")
            break;

# From self.play_trick()
def opponent_plays(game):
    while True:
        response = input("What card does P2 play? (enter as string): ")
        print()
        if response in game["p2"].hand:
            card_index = game["p2"].hand.index(response)
            card.play_card(game, card_index, "p2")
            break

# From self.play_trick(), minimax.if_trick_complete()
def setup_next_trick(game):
    players_list = ["p1", "p2"]
    if len(game["p1"].hand) == 0 or len(game["p2"].hand) == 0:
        game["hand_finished"] = True
    evaluate.determine_winner_of_trick(game)
    game["lead_player"] = game["player_winning_trick"]
    add_cards_to_trick_pile(game)
    for player in players_list:
        game[player].cards_in_play_ranks = [0, 0]
    print("***** " + game["player_winning_trick"] + " WINS TRICK ******")
    print("***** " + game["lead_player"] + " LEADS NEXT TRICK ******")
    print()

# From self.setup_next_trick()
def add_cards_to_trick_pile(game):
    for i in range(2):
        game[game["player_winning_trick"]].trick_pile.append(game["p1"].cards_in_play.pop())
        game[game["player_winning_trick"]].trick_pile.append(game["p2"].cards_in_play.pop())


    