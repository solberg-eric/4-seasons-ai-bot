"""Play a card."""

# From trick.player_plays(), trick.opponent_plays()
def play_card(game, card_index, player):
    game[player].cards_in_play.append(game[player].hand.pop(card_index))