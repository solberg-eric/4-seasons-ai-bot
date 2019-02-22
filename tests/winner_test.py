import winner

def test_has_won(game):
    game["p1"].hand = []
    game["p2"].hand = ["AH"]
    winner.has_won(game)
    assert game["p1"].has_won == False
    assert game["p2"].has_won == True