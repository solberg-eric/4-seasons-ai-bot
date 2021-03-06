import pytest
from copy import deepcopy
import sys
sys.path.insert(0, "/Users/ericsolberg/Desktop/card_game_python")
print(sys.path)

@pytest.fixture
def games(cards_in_play1, cards_in_play2, cards_in_play3, cards_in_play4):
    games = [cards_in_play1, cards_in_play2, cards_in_play3, cards_in_play4]
    return games

@pytest.fixture
def cards_in_play1(game):
    game1 = deepcopy(game)
    game1["p1"].cards_in_play = ["AH", "JC"]
    game1["p2"].cards_in_play = ["AS", "AD"]
    return game1

@pytest.fixture
def cards_in_play2(game):
    game2 = deepcopy(game)
    game2["p1"].cards_in_play = ["AS", "AD"]
    game2["p2"].cards_in_play = ["AH", "JC"]
    return game2

@pytest.fixture
def cards_in_play3(game):
    game3 = deepcopy(game)
    game3["p1"].cards_in_play = ["KH", "KC"]
    game3["p2"].cards_in_play = ["KC", "KH"]
    return game3

@pytest.fixture
def cards_in_play4(game):
    game4 = deepcopy(game)
    game4["p1"].cards_in_play = ["KC", "KH"]
    game4["p2"].cards_in_play = ["KH", "KC"]
    return game4

@pytest.fixture
def player():
    class Player:
        def __init__(self, hand, cards_in_play, cards_in_play_ranks, trick_pile, cost, gain, has_won):
            self.hand = hand # (list) of (strings): Cards in hand.
            self.cards_in_play = cards_in_play # (list) of (strings): Cards in play.
            self.cards_in_play_ranks = cards_in_play_ranks # (list of (ints): Value of cards in play.
            self.trick_pile = trick_pile # (list) of (strings): Cards won/captured by player.
            self.cost = cost # (int): The 'value' that a player loses from their hand with they play.
            self.gain = gain # (int): The 'value' that a player gains when they win a trick.
            self.has_won = has_won # (boolean): 'True' if the player has won the game, false otherwise.
    return Player

@pytest.fixture
def game(player):

    # Create Player One (p1) and Player Two (p2) with initial startingi values.
    p1 = player(["JC", "QC", "KC", "AC", "JD", "QD", "KD", "AD", "JS", "QS", "KS", "AS", "JH", "QH", "KH", "AH"], [], [0, 0], [], 0, 0, False)
    p2 = player(["AH", "KH", "QH", "JH", "AS", "KS", "QS", "JS", "AD", "KD", "QD", "JD", "AC", "KC", "QC", "JC"], [], [0, 0], [], 0, 0, False)

    # Store frequently used values pertaining to the game.
    game = {
        "p1" : p1,
        "p2" : p2,
        "depth_factor" : 1, # Depth of search for minimax algoirthm (in tricks)
        "depth" : 4, # Depth of search for minimax algorithm (in turns). There are four turns per trick.
        "alpha" : -float("Inf"), # Used in minimax algorithm
        "beta" : float("Inf"), # Used in minimax algorithm
        "trump_order" : ["Hearts", "Spades", "Diamonds", "Clubs"],
        "lead_player" : "p2", # (string): "p1" for player one; "p2" for player two.
        "lead_suit" : None, # (string): "H", "S", "D", or "C".
        "player_winning_trick" : None, # Eventually (string): "p1" or "p2".
        "hand_finished" : False,
        "value" : 0, # (int): Value of potential game state (used in evaluation function during minimax algorithm).
        "player_optimizing" : "p1", # (string): Either "p1" or "p2". Denotes which player is being optimized in minimax algorithm.
        "user_has_played" : False, # added for pygame purposes
        "turn" : "p2c1" # added for pygame purposes. remember that user is p2
    }
    return game