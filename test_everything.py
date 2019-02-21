import pytest
import card
import winner
import hand
import trick

# Test card.play_card() and card.arrange_cards_for_next_hand()
def test_play_card_and_arrange_cards_for_next_hand(game):
    card.play_card(game, 5, "p1")
    assert game["p1"].cards_in_play == ["QD"]
    assert game["p1"].hand == ["JC", "QC", "KC", "AC", "JD", "KD", "AD", "JS", "QS", "KS", "AS", "JH", "QH", "KH", "AH"] 

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

# Test winner.has_won()
def test_has_won(game):
    game["p1"].hand = []
    game["p2"].hand = ["AH"]
    winner.has_won(game)
    assert game["p1"].has_won == False
    assert game["p2"].has_won == True


