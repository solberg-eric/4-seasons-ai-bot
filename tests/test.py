import pytest
import card

@pytest.fixture
def player_template:
    class Player:
        def __init__(self, hand, cards_in_play, cards_in_play_ranks, trick_pile, cost, gain, has_won):
            self.hand = hand # (list) of (strings): Cards in hand.
            self.cards_in_play = cards_in_play # (list) of (strings): Cards in play.
            self.cards_in_play_ranks = cards_in_play_ranks # (list of (ints): Value of cards in play.
            self.trick_pile = trick_pile # (list) of (strings): Cards won/captured by player.
            self.cost = cost # (int): The 'value' that a player loses from their hand with they play.
            self.gain = gain # (int): The 'value' that a player gains when they win a trick.
            self.has_won = has_won # (boolean): 'True' if the player has won the game, false otherwise.

@pytest.fixture
def game(player_template){
    """Prepare for game.

    Args: 
        depth_factor (int): The depth of search (in tricks) for the minimax algorithm.

    Returns: 
        game (dict): Stores frequently used values pertaining to the game.
    """
    # Creates Player One (p1) and Player Two (p2) with initial startingi values.
    p1 = player_template.Player(["JC", "QC", "KC", "AC", "JD", "QD", "KD", "AD", "JS", "QS", "KS", "AS", "JH", "QH", "KH", "AH"], [], [0, 0], [], 0, 0, False)
    p2 = player_template.Player(["AH", "KH", "QH", "JH", "AS", "KS", "QS", "JS", "AD", "KD", "QD", "JD", "AC", "KC", "QC", "JC"], [], [0, 0], [], 0, 0, False)

    # Store frequently used values pertaining to the game.
    game = {
        "p1" : p1,
        "p2" : p2,
        "depth_factor" : depth_factor, # Depth of search for minimax algoirthm (in tricks)
        "depth" : depth_factor * 4, # Depth of search for minimax algorithm (in turns). There are four turns per trick.
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

# Test card.play_card() and card.arrange_cards_for_next_hand()
def test_play_card_and_arrange_cards_for_next_hand(game):
    card.play_card(game, 5, "p1")
    assert game["p1"].cards_in_play == "QD"
    assert game["p1"].hand == ["JC", "QC", "KC", "AC", "JD", "KD", "AD", "JS", "QS", "KS", "AS", "JH", "QH", "KH", "AH"] 

# Test hand.setup_next_hand()
def test_setup_next_hand(player_template):
    p1 = player_template.Player([], [], [0, 0], ["AH", "JC", "QH", "KS"], 5, 10, False)
    p2 = player_template.Player([], [], [0, 0], ["QC", "QS"], 20, -4, False)
    game = {
        "p1" : p1,
        "p2" : p2,
        "trump_order" : ["Clubs", "Hearts", "Spades", "Diamonds"],
        "hand_finished" : True
    }
    card.setup_next_hand(game)
    assert game["trump_order"] == ["Hearts", "Spades", "Diamonds", "Clubs"]
    assert game["hand_finished"] == False
    players_list = ["p1", "p2"]
    for player in players_list:
        assert game[player].cards_in_play == []
        assert game[player].cards_in_play_ranks == [0, 0]
        assert game[player].trick_pile == []
    assert game["p1"].hand = ["JC", "KS", "QH", "AH"]
    assert game["p2"].hand = ["QS", "QC"]

# Test winner.has_won()
def test_has_won(player_template):
    p1 = player_template.Player([], [], [0,0], [], 0, 0, False)
    p2 = player_template.Player(["AH"], [], [0,0], [], 0, 0, False)
    game = {
        "p1" : p1,
        "p2" : p2
    }
    winner.has_won(game)
    assert game["p1"].has_won == False
    assert game["p2"].has_won == True

