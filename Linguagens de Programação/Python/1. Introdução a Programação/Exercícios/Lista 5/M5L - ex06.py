'''
Seja o polinômio: P(X) = anXn + an-1Xn-1 + an-2Xn-2 + .... + a1X + a0
Escreva um programa que leia um número real x, a ordem do polinômio n (no máximo
20), os coeficientes ai e calcule o resultado. Imprima o polinômio lido e o valor
calculado.
'''

print("Programa para calcular polinomios")
print("Nosso polinomio terá a seguinte estrutura:")
print("P(X) = anX^n + an-1X^n-1 + an-2X^n-2 + .... + a1X + a0")
print("Assim, \n 'a' é o coeficiente \n 'n' a ordem \n 'x' o número real")
print("-"*80)

#Lendo os dados
coeficiente = int(input("Insira o coeficiente: "))
numero = float(input("Insira a base do número (número real): "))
ordem = int(input("Insira a ordem do polinomio (max -> 20): "))
if ordem > 20:
    print("O valor excede 20, tente novamente.")
    ordem = int(input("Insira a ordem do polinomio (max -> 20)"))

#calculando o polinomio

resultado = []
coeficientes = []
numeros = []
ordens = []
while ordem > -1:
    polinomio = coeficiente * (numero**ordem)
    resultado.append(polinomio)
    coeficientes.append(coeficiente)
    numeros.append(numero)
    ordens.append(ordem)

    ordem = ordem - 1
    coeficiente = coeficiente - 1

#Imprimindo o polinomio lido
    
termos = []
print("O polinomio é escrito da seguinte maneira:")
for i in coeficientes:
    termo = f"{coeficientes[i]}•{numeros[i]}^{ordens[i]}"
    termos.append(termo)
total = " + ".join(termos)
print(total)

#calculando o resultado
    
print("-"*80)
print("O resultado desse polinomio é:", sum(resultado))
