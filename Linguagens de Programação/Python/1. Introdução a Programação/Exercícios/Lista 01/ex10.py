# A convenção de graus Fahrenheit para Celsius é obtida pela fórmula C = 5. (F − 32)/9.
# Escreva um programa que calcule e imprima uma tabela de graus centígrados em
# função de graus Fahrenheit que variem de 50 a 150 de 5 em 5. Utilize constantes
# simbólicas para indicar o início (50) e o fim (150) do intervalo, além do passo (5).

def conversão():
    for i in range(50,151,5):
        Fahrenheit = ((i/5) * 9) + 32
        print(" ",i,"       ", Fahrenheit)

def main():
    print('Tabela:')
    print('Celsius // Fahrenheit')
    conversão()
    print('fim do programa')

main()