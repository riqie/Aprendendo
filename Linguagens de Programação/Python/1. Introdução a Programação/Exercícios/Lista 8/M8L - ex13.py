'''
13. Uma equação do segundo grau é escrita ax² + bx + c = 0 e a sua solução é dada em função dos valores de a, b e c. Podendo ter duas raízes, uma ou nenhuma. Escreva uma função que resolva a equação do segundo grau, retornando o número de raízes encontradas. Os valores dessas raízes devem ser retornados em parâmetros.
'''

def abc():
    while True:
        try:
            a = int(input('Informe o valor de a:'))
            b = int(input('Informe o valor de b:'))
            c = int(input('Informe o valor de c:'))
            if a == 0:
                print(50*"=")
                print("Coeficiente 'a' deve ser diferente de zero!")
                print(50*"=")                
            else:
                return a, b, c
        except ValueError:
            print(50*"=")
            print("Coeficientes 'a', 'b' e 'c' devem ser inteiros!")
            print(50*"=")
            
def calculo(A,B,C):
    delta = pow(B, 2) - 4 * A * C
    
    x1 = (-B + (delta)**(1/2))/(2*A)
    x2 = (-B - (delta)**(1/2))/(2*A)

    return delta, x1, x2

def analise_delta(Delta, xi, xii):
    if Delta > 0:
        print('\nDelta > 0. Logo, a equação possui duas raízes reais e distintas')
        print(f'x1 = {xi:.2f}, x2 = {xii:.2f}')
        
    elif Delta == 0:
        print('\nDelta = 0. Logo, a equação possui duas raízes reais e iguais')
        print(f'x1 = {xi:.2f}, x2 = {xii:.2f}')
        
    else:
        print('\nDelta < 0. Logo, a equação não possui raízes reais')

def main():
    print(f"\t{35*"-"}")
    print("\tEquação quadrática ax² + bx + c = 0")
    print(f"\t{35*"-"}\n")

    a, b, c = abc()

    delta, x1, x2 = calculo(A = a, B = b, C = c)

    analise_delta(Delta = delta, xi = x1, xii = x2) 

main()

