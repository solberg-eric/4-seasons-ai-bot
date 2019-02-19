"""Prepares for game."""

# From main
def setup_game(depth_factor):
    """Prepare for game.

    Args: 
        depth_factor (int): The depth of search (in tricks) for the minimax algorithm.

    Returns: 
        game (dict): Stores frequently used values pertaining to the game.
    """
    class Player:
        def __init__(self, hand, cards_in_play, cards_in_play_ranks, trick_pile, cost, gain, has_won):
            self.hand = hand # (list) of (strings): Cards in hand.
            self.cards_in_play = cards_in_play # (list) of (strings): Cards in play.
            self.cards_in_play_ranks = cards_in_play_ranks # (list of (ints): Value of cards in play.
            self.trick_pile = trick_pile # (list) of (strings): Cards won/captured by player.
            self.cost = cost # (int): The 'value' that a player loses from their hand with they play.
            self.gain = gain # (int): The 'value' that a player gains when they win a trick.
            self.has_won = has_won # (boolean): 'True' if the player has won the game, false otherwise.

    # Creates Player One (p1) and Player Two (p2) with initial startingi values.
    p1 = Player(["AH", "KH", "QH", "JH", "AS", "KS", "QS", "JS", "AD", "KD", "QD", "JD", "AC", "KC", "QC", "JC"], [], [0, 0], [], 0, 0, False)
    p2 = Player(["JC", "QC", "KC", "AC", "JD", "QD", "KD", "AD", "JS", "QS", "KS", "AS", "JH", "QH", "KH", "AH"], [], [0, 0], [], 0, 0, False)

    # Store frequently used values pertaining to the game.
    game = {
        "p1" : p1,
        "p2" : p2,
        "depth_factor" : depth_factor, # Depth of search for minimax algoirthm (in tricks)
        "depth" : depth_factor * 4, # Depth of search for minimax algorithm (in turns). There are four turns per trick.
        "alpha" : -float("Inf"), # Used in minimax algorithm
        "beta" : float("Inf"), # Used in minimax algorithm
        "trump_order" : ["Hearts", "Spades", "Diamonds", "Clubs"],
        "lead_player" : lead_player(), # (string): "p1" for player one; "p2" for player two.
        "lead_suit" : None, # (string): "H", "S", "D", or "C".
        "player_winning_trick" : None, # Eventually (string): "p1" or "p2".
        "hand_finished" : False,
        "value" : 0, # (int): Value of potential game state (used in evaluation function during minimax algorithm).
        "player_optimizing" : "p1" # (string): Either "p1" or "p2". Denotes which player is being optimized in minimax algorithm.
    }
    return game

# From self.setup_game
def lead_player():
    """Asks the user who the lead player of the game is. 
    
    Args: 
        none
    
    Returns: 
        (string): 'p1' or 'p2'.
    """
    while True:
        response = input("Are you the starting player? (y/n): ")
        print()
        if response == "y":
            return "p1"
            break
        elif response == "n":
            return "p2"
            break
