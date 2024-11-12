'''
# Escreva uma função recursiva que demonstre solução da Torre de Hanoi para n
# discos, indicados pelo usuário.
'''

def torre_hanoi(n, origem, destino, auxiliar):
    '''
    se tiver apenas 1 disco, basta mover para o destino.
    '''

    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    
    '''
    a função chama ela mesma passando as torres como parametros e diminuindo o número de discos até que todos os dicos possíveis tenham sido movidos, depois a função irá chamar ela novamente, porém com os parametros trocados, isto ocorre para que a lógica do tamanho dos discos funcione, ou seja, o programa vai mudar os discos de lugar sem colocar um disco maior sobre outro menor:
    '''

    torre_hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    torre_hanoi(n - 1, auxiliar, destino, origem)

def main():
    print('\nO programa realizará a solução da Torre de Hanoi. ')

    while True:
        n = input('\nDigite quantos discos: ')

        if n.isdigit() == False or int(n) <= 0:
            print('Entrada inválida, entre com um número inteiro positivo.')
            continue

        else:
            torre_hanoi(int(n), 'torre A', 'torre C', 'torre B')
            break

    print('Fim do programa.')

main()
