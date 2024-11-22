'''8. Implemente uma classe chamada GuessingGame que represente um jogo de 
adivinhação. Essa classe deve gerar um número aleatório, permitir que o jogador faça 
palpites e informar se o palpite está correto, informando se é maior ou menor que o 
número gerado.'''
   
from guessinggame import GuessingGame

def main():
    number = GuessingGame.generate_number()
    guess = -1  # Exemplo de palpite
    while guess != number:
        guess = int(input('Seu palpite: '))
        result = GuessingGame.check_guess(number, guess)
        print(result)
        if result != 'Correto':
            continue
        else:
            break
    
main()
