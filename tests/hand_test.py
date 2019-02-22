import hand

# Test hand.setup_next_hand()
def test_setup_next_hand(game):
    game["p1"].trick_pile = ["AH", "JC", "QH", "KS"]
    game["p2"].trick_pile = ["QC", "QS"]
    game["trump_order"] = ["Clubs", "Hearts", "Spades", "Diamonds"]
    game["hand_finished"] = True
    hand.setup_next_hand(game)
    assert game["trump_order"] == ["Hearts", "Spades", "Diamonds", "Clubs"]
    assert game["hand_finished"] == False
    players_list = ["p1", "p2"]
    for player in players_list:
        assert game[player].cards_in_play == []
        assert game[player].cards_in_play_ranks == [0, 0]
        assert game[player].trick_pile == []
    assert game["p1"].hand == ["JC", "KS", "QH", "AH"]
    assert game["p2"].hand == ["QS", "QC"]