import card

def test_play_card_and_arrange_cards_for_next_hand(game):
    # Play two cards from p1's hand
    card.play_card(game, 5, "p1")
    assert game["p1"].cards_in_play == ["QD"]
    assert game["p1"].hand == ["JC", "QC", "KC", "AC", "JD", "KD", "AD", "JS", "QS", "KS", "AS", "JH", "QH", "KH", "AH"] 

    card.play_card(game, 5, "p1")
    assert game["p1"].cards_in_play == ["QD", "KD"]
    assert game["p1"].hand == ["JC", "QC", "KC", "AC", "JD", "AD", "JS", "QS", "KS", "AS", "JH", "QH", "KH", "AH"] 

    # Play two cards from p2's hand
    card.play_card(game, 0, "p2")
    assert game["p2"].cards_in_play == ["AH"]
    assert game["p2"].hand == ["KH", "QH", "JH", "AS", "KS", "QS", "JS", "AD", "KD", "QD", "JD", "AC", "KC", "QC", "JC"]

    card.play_card(game, 14, "p2")
    assert game["p2"].cards_in_play == ["AH", "JC"]
    assert game["p2"].hand == ["KH", "QH", "JH", "AS", "KS", "QS", "JS", "AD", "KD", "QD", "JD", "AC", "KC", "QC"]