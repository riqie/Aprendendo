'''8. Implemente uma classe chamada GuessingGame que represente um jogo de 
adivinhação. Essa classe deve gerar um número aleatório, permitir que o jogador faça 
palpites e informar se o palpite está correto, informando se é maior ou menor que o 
número gerado.'''
import random

class GuessingGame:
    @staticmethod
    def generate_number():
        return random.randint(1, 10)

    @staticmethod
    def check_guess(number, guess):
        if guess < number:
            return "Maior"
        elif guess > number:
            return "Menor"
        else:
            return 'Correto'

