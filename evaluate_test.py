import evaluate

def test_evaluate_game(games):
    games[0]["lead_suit"] = "S"
    games[0]["lead_player"] = "p2"
    assert evaluate.evaluate_game(games[0]) == 28

    games[1]["lead_suit"] = "S"
    games[1]["lead_player"] = "p1"
    assert evaluate.evaluate_game(games[1]) == -28

    games[2]["lead_suit"] = "C"
    games[2]["lead_player"] = "p2"
    assert evaluate.evaluate_game(games[2]) == 16

    games[3]["lead_suit"] = "H"
    games[3]["lead_player"] = "p2"
    assert evaluate.evaluate_game(games[3]) == -16

def test_determine_winner_of_trick(games):
    games[0]["lead_suit"] = "S"
    games[0]["lead_player"] = "p2"
    for i in range(4):
        evaluate.determine_winner_of_trick(games[i])
        if i == 0:
            assert games[i]["player_winning_trick"] == "p1"
            games[i+1]["lead_suit"] = "S" # sets up next lead suit
            games[i+1]["lead_player"] = "p1"
        if i == 1:
            assert games[i]["player_winning_trick"] == "p2"
            games[i+1]["lead_suit"] = "C"
            games[i+1]["lead_player"] = "p2"
        if i == 2:
            assert games[i]["player_winning_trick"] == "p1"
            games[i+1]["lead_suit"] = "H"
            games[i+1]["lead_player"] = "p2"
        if i == 3:
            assert games[i]["player_winning_trick"] == "p2"
        games[i]["player_winning_trick"] = None

def test_set_card_ranks(games):
    games[0]["lead_suit"] = "S"
    evaluate.set_card_ranks(games[0])
    assert games[0]["p1"].cards_in_play_ranks[0] == 8
    assert games[0]["p1"].cards_in_play_ranks[1] == 0
    assert games[0]["p2"].cards_in_play_ranks[0] == 4
    assert games[0]["p2"].cards_in_play_ranks[1] == 0

    games[1]["lead_suit"] = "S"
    evaluate.set_card_ranks(games[1])
    assert games[1]["p1"].cards_in_play_ranks[0] == 4
    assert games[1]["p1"].cards_in_play_ranks[1] == 0
    assert games[1]["p2"].cards_in_play_ranks[0] == 8
    assert games[1]["p2"].cards_in_play_ranks[1] == 0

    games[2]["lead_suit"] = "C"
    evaluate.set_card_ranks(games[2])
    assert games[2]["p1"].cards_in_play_ranks[0] == 7
    assert games[2]["p1"].cards_in_play_ranks[1] == 3
    assert games[2]["p2"].cards_in_play_ranks[0] == 3
    assert games[2]["p2"].cards_in_play_ranks[1] == 7

    games[3]["lead_suit"] = "H"
    evaluate.set_card_ranks(games[3])
    assert games[3]["p1"].cards_in_play_ranks[0] == 0
    assert games[3]["p1"].cards_in_play_ranks[1] == 7
    assert games[3]["p2"].cards_in_play_ranks[0] == 7
    assert games[3]["p2"].cards_in_play_ranks[1] == 0

def test_determine_gain(games):
    # Test p1 winning trick
    for i in range(4):
        games[i]["player_winning_trick"] = "p1"

    evaluate.determine_gain(games[0])
    assert games[0]["p1"].gain == 25
    assert games[0]["p2"].gain == 0

    evaluate.determine_gain(games[1])
    assert games[1]["p1"].gain == 25
    assert games[1]["p2"].gain == 0

    evaluate.determine_gain(games[2])
    assert games[2]["p1"].gain == 16
    assert games[2]["p2"].gain == 0

    evaluate.determine_gain(games[3])
    assert games[3]["p1"].gain == 16
    assert games[3]["p2"].gain == 0

    # Test p2 winning trick
    for i in range(4):
        games[i]["p1"].gain = 0 # have to reset to zero
        games[i]["player_winning_trick"] = "p2"

    evaluate.determine_gain(games[0])
    assert games[0]["p1"].gain == 0
    assert games[0]["p2"].gain == 25

    evaluate.determine_gain(games[1])
    assert games[1]["p1"].gain == 0
    assert games[1]["p2"].gain == 25

    evaluate.determine_gain(games[2])
    assert games[2]["p1"].gain == 0
    assert games[2]["p2"].gain == 16

    evaluate.determine_gain(games[3])
    assert games[3]["p1"].gain == 0
    assert games[3]["p2"].gain == 16

def test_determine_cost(games):
    evaluate.determine_cost(games[0])
    assert games[0]["p1"].cost == 11
    assert games[0]["p2"].cost == 14

    evaluate.determine_cost(games[1])
    assert games[1]["p1"].cost == 14
    assert games[1]["p2"].cost == 11

    evaluate.determine_cost(games[2])
    assert games[2]["p1"].cost == 12
    assert games[2]["p2"].cost == 12

    evaluate.determine_cost(games[3])
    assert games[3]["p1"].cost == 12
    assert games[3]["p2"].cost == 12

