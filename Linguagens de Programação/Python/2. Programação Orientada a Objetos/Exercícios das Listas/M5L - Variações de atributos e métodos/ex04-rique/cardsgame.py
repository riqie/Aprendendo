'''
4. Implemente uma classe chamada CardsGame que represente um jogo de cartas
simples, como o Uno. Essa classe deve ter métodos para embaralhar as cartas,
distribuir as cartas aos jogadores e permitir jogadas.
'''
import random

class CardsGame:
    def __init__(self, num_players):
        self.deck = self.create_deck()
        self.players = {}
        
        for i in range(num_players):
            self.players[f'Player {i + 1}'] = []

    @staticmethod
    def create_deck():
        colors = ['Red', 'Green', 'Blue', 'Yellow']
        values = []

        for i in range(1, 10):
            values.append(str(i))
        
        values.append('Skip')
        values.append('Reverse')
        values.append('Draw Two')

        deck = []
        
        for color in colors:
            for value in values:
                deck.append(f'{color}: {value}')
        
        random.shuffle(deck)
        return deck

    def deal_cards(self, num_cards):
        # Distribui cartas para os jogadores
        for player in self.players:
            for _ in range(num_cards):
                if self.deck:
                    card = self.deck.pop()
                    self.players[player].append(card)

    def play_card(self, player, card):
        # Permite que o jogador jogue uma carta
        if card in self.players[player]:
            self.players[player].remove(card)
            print(f'{player} played {card}')
        else:    
            print(f'{player} does not have {card}')
