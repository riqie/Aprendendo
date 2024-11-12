'''
Escreva uma função que leia e retorne uma matriz de inteiros fornecida pelo 
usuário. Sua matriz deve ler os números linha a linha. Os números devem estar 
separados por espaços em branco. Sua função deve interromper a leitura ao 
receber uma linha em branco
'''

def ler_matriz():
    matriz = []
    while True:
        linha = input("Digite uma linha de números separados por espaço (ou pressione Enter para finalizar): ")
        if linha == "":
            break
        try:
            numeros = list(map(int, linha.split()))
            matriz.append(numeros)
        except ValueError:
            print("Por favor, insira apenas números inteiros.")
    return matriz

def main():
    print("Lendo matriz de inteiros")
    print("-"*80)
    matriz = ler_matriz()
    for linha in matriz:
        print(linha)

print(main())
