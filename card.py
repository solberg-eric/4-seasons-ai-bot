"""Play a card."""

# From click.check_card()
def play_card(game, card_index, player):
    game[player].cards_in_play.append(game[player].hand.pop(card_index))