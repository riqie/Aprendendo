# Faça um programa didático para estudo das raízes quadradas dos números, da 
# seguinte forma: o programa gera um número aleatório, eleva ao quadrado e pergunta 
# qual a raiz quadrada desse valor para o estudante. O programa deve apresentar as 
# mensagens de erro e incentivo e os números de perguntas, acertos e erros de forma 
# semelhante aos anteriores. 

import random

def gerarNumero():
    numero_aleatorio = random.randint(1, 1000)

    return numero_aleatorio

def gerarResposta(numero):
    resposta = numero ** 0.5

    return int(resposta)

def verificarResposta(respostaUsuario, respostaCorreta):
    if respostaUsuario == respostaCorreta:
        return print('Parabéns, você acertou!')
    
    else:
        return print(f'"{respostaUsuario}" não corresponde a resposta correta.\nMas não desanime, continue tentando para melhorar seus resultados!')

def main():
    print('\nO programa serve como estudo didático para encontrar as raízes quadradas dos números de 1 até 1000.\nDigite "0" para sair.')
    print('\nOBS: Para raízes não exatas, aproxime o valor.')

    while True:
        numero = gerarNumero()
        respostaCorreta = gerarResposta(numero)

        print(f'\nQual a raiz quadrada do número {numero}?')

        respostaUsuário = input('\nDigite a resposta: ')

        if respostaUsuário == "0":
            return print('fim do programa.')

        verificarResposta(respostaUsuário, respostaCorreta)

main()
# finalizado
