"""Pygame module to check location of user mouse-click. Based on that, potentially do some action."""
import card

# From trick.your_turn()
def check_location_of_click(game, mouse_pos): # pygame
    x, y = mouse_pos
    # Player 1 will play first card
    if game["turn"] == "p2c1":
        if 27 <= x < len(game["p2"].hand)*27+184 and 648 <= y < 700:
            check_card(game, mouse_pos)
            game["user_has_played"] = True
            game["turn"] = "p1c1"
    # Player 2 will play first card
    elif game["turn"] == "p1c1":
        if 27 <= x < len(game["p1"].hand)*27+184 and 0 <= y < 52:
            check_card(game, mouse_pos)
            game["user_has_played"] = True
            game["turn"] = "p2c2"
    # Player 1 will play second card
    elif game["turn"] == "p2c2":
        if 27 <= x < len(game["p2"].hand)*27+184 and 648 <= y < 700:
            check_card(game, mouse_pos)
            game["user_has_played"] = True
            game["turn"] = "p1c2"
    # Player 2 will play second card
    elif game["turn"] == "p1c2":
        if 27 <= x < len(game["p1"].hand)*27+184 and 0 <= y < 52:
            check_card(game, mouse_pos)
            game["user_has_played"] = True
            game["turn"] = "p2c1"
            # setup next trick

# From self.check_location_of_click
def check_card(game, mouse_pos):
    x, y = mouse_pos
    # User plays 1st card
    if game["turn"] == "p2c1":
        cards_in_hand = len(game["p2"].hand)
        if cards_in_hand*27 <= x < cards_in_hand*27+184 and 648 <= y < 700:
            card.play_card(game, cards_in_hand-1, "p2")
        for i in range(1, cards_in_hand):
            if i*27 <= x < (i+1)*27 and 648 <= y < 700:
                card.play_card(game, i-1, "p2")
                break
    # Player 1 plays 1st card
    elif game["turn"] == "p1c1":
        if 27 <= x < 27+184 and 0 <= y < 52:
            card.play_card(game, 0, "p1")
        for i in range(len(game["p1"].hand)-1, 0, -1): # might have to change just like i did to p2...meaning it might not play last trick in hand. (put elif block in front of for loop to fix)
            if i*27+184 <= x < (i+1)*27+184 and 0 <= y < 52:
                card.play_card(game, i, "p1")
                break
    # User plays 2nd card
    elif game["turn"] == "p2c2":
        cards_in_hand = len(game["p2"].hand)
        if cards_in_hand*27 <= x <= cards_in_hand*27+184 and 648 <= y <= 700:
            card.play_card(game, cards_in_hand-1, "p2")
        for i in range(1, cards_in_hand):
            if i*27 <= x <= (i+1)*27 and 648 <= y <= 700:
                card.play_card(game, i-1, "p2")
                break
    # Player 1 plays 2nd card
    elif game["turn"] == "p1c2":
        if 27 <= x < 27+184 and 0 <= y < 52:
            card.play_card(game, 0, "p1")
        for i in range(len(game["p1"].hand)-1, 0, -1):
            if i*27+184 <= x < (i+1)*27+184 and 0 <= y < 52:
                card.play_card(game, i, "p1")
                break
