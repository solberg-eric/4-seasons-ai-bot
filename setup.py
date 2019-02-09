"""Instantiates necessary variables and prepares for game"""

# From main
def setup_game(depth_factor):
    class Player:
        def __init__(self, hand, cards_in_play, cards_in_play_ranks, trick_pile, cost, gain, has_won):
            self.hand = hand
            self.cards_in_play = cards_in_play
            self.cards_in_play_ranks = cards_in_play_ranks
            self.trick_pile = trick_pile
            self.cost = cost
            self.gain = gain
            self.has_won = has_won

    p1 = Player(["AH", "KH", "QH", "JH", "AS", "KS", "QS", "JS", "AD", "KD", "QD", "JD", "AC", "KC", "QC", "JC"], [], [0, 0], [], 0, 0, False)
    p2 = Player(["AH", "KH", "QH", "JH", "AS", "KS", "QS", "JS", "AD", "KD", "QD", "JD", "AC", "KC", "QC", "JC"], [], [0, 0], [], 0, 0, False)

    game = {
        "p1" : p1,
        "p2" : p2,
        "depth_factor" : depth_factor,
        "depth" : depth_factor * 4,
        "alpha" : -float("Inf"),
        "beta" : float("Inf"),
        "trump_order" : ["Hearts", "Spades", "Diamonds", "Clubs"],
        "lead_player" : lead_player(),
        "lead_suit" : None, # "H", "S", "D", or "C"
        "player_winning_trick" : None, # Eventually going to be "p1" or "p2"
        "hand_finished" : False,
        "value" : 0,
        "player_optimizing" : "p1"
    }
    return game

# From self.setup_game
def lead_player():
    while True:
        response = input("Are you the starting player? (y/n): ")
        print()
        if response == "y":
            return "p1"
            break
        elif response == "n":
            return "p2"
            break
