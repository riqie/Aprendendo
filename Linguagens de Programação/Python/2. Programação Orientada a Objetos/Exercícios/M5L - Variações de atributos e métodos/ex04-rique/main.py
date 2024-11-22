'''
4. Implemente uma classe chamada CardsGame que represente um jogo de cartas
simples, como o Uno. Essa classe deve ter métodos para embaralhar as cartas,
distribuir as cartas aos jogadores e permitir jogadas.
'''

from cardsgame import CardsGame

def main():
    game = CardsGame(4)
    game.deal_cards(7)
    
    for player, cards in game.players.items():
        print(f'{player}: {cards}')  # Mostra as cartas de cada jogador

    played_card = game.players['Player 1'][0]
    game.play_card('Player 1', played_card)

    for player, cards in game.players.items():
        print(f'{player}: {cards}')  # Mostra as cartas de cada jogador



main()
