import L4
from L7 import *

#6.0
def evaluate_game(game): # From 5.1, 5.4
    L4.determine_winner_of_trick(game) # To 4.5
    #print(game["player_winning_trick"])
    determine_gain(game) # To 7.0
    determine_cost(game) # To 7.1
    return (game["p1"].gain - game["p1"].cost) - (game["p2"].gain - game["p2"].cost)

