import trick

# def test_play_trick():

def test_determine_play_order(game):
    game["lead_player"] = "p1"
    assert trick.determine_play_order(game) == ["p1", "p2"]
    game["lead_player"] = "p2"
    assert trick.determine_play_order(game) == ["p2", "p1"]

# def test_your_turn():

def test_computer_plays(game):
    game["p1"].hand = ["QC", "KC", "KD"]
    result = [1, "KD"]
    trick.computer_plays(game, result)
    assert game["p1"].hand == ["QC", "KC"]
    assert game["p1"].cards_in_play == ["KD"]

# finish after testing determine winner of trick
#def test_setup_next_trick(game):
#
#    # Test game["hand_finished"]
#    game["p1"].hand = ["AH", "KH"]
#    game["p2"].hand = ["AH", "KH"]
#    assert game["hand_finished"] == False
#    assert game["hand_finished"] == True
#    assert game["hand_finished"] == True


def test_add_cards_to_trick_pile(game):
    # Test p1 winning trick
    game["player_winning_trick"] = "p1"
    game["p1"].trick_pile = []
    game["p2"].trick_pile = []
    game["p1"].cards_in_play = ["KS", "JC"]
    game["p2"].cards_in_play = ["QC", "QS"]
    trick.add_cards_to_trick_pile(game)
    assert game["p1"].cards_in_play == []
    assert game["p2"].cards_in_play == []
    assert game["p1"].trick_pile == ["JC", "QS", "KS", "QC"]
    assert game["p2"].trick_pile == []

    # Test p2 winning trick
    game["player_winning_trick"] = "p2"
    game["p1"].trick_pile = []
    game["p2"].trick_pile = []
    game["p1"].cards_in_play = ["AH", "QH"]
    game["p2"].cards_in_play = ["KC", "KC"]
    trick.add_cards_to_trick_pile(game)
    assert game["p1"].cards_in_play == []
    assert game["p2"].cards_in_play == []
    assert game["p1"].trick_pile == []
    assert game["p2"].trick_pile == ["QH", "KC", "AH", "KC"]

    # Test one more for fun
    game["player_winning_trick"] = "p2"
    game["p1"].trick_pile = ["JC", "QS", "KH", "KH"]
    game["p2"].trick_pile = ["QH", "QS", "AH", "JS"]
    game["p1"].cards_in_play = ["AC", "KC"]
    game["p2"].cards_in_play = ["JH", "KS"]
    trick.add_cards_to_trick_pile(game)
    assert game["p1"].cards_in_play == []
    assert game["p2"].cards_in_play == []
    assert game["p1"].trick_pile == ["JC", "QS", "KH", "KH"]
    assert game["p2"].trick_pile == ["QH", "QS", "AH", "JS", "KC", "KS", "AC", "JH"]