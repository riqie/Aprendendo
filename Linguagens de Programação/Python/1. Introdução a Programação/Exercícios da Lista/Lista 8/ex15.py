# Escreva um programa com uma função para receber do usuário um conjunto de 
# valores reais e também com funções próprias que recebem como argumento uma 
# lista e calculem e retornem a média, o maior, o menor e a soma dos elementos da 
# lista

# criando as funçoes com as equações:
def calcular_media(lista):
    media = sum(lista) / len(lista)
    return media

def calcular_maior(lista):
    maior = max(lista)
    return maior

def calcular_menor(lista):
    menor = min(lista)
    return menor

def calcular_soma(lista):
    soma = sum(lista)
    return soma

# função para a interface e armazenar os valores que serao dados
def receber_valores():
    valores = [] # variavel para armazenar os valores fornecidos pelo usuario
    print('='*60)
    print("Digite os valores reais.\nPressione 'ENTER' para ver os resultados:")
    
    # criei um loop para rodar o programa
    while True:
        
        entrada = input('Valor: ') # valor fornecido

        # condição para parar o looping
        if entrada.lower() == '':
            break
        
        # Try serve para não ocorrer o erro
        try:
            valor = float(entrada)
            valores.append(valor)
              
        except ValueError:
            print('='*60)
            print("Valor inválido, tente novamente.")
    
    return valores  

# função para atribuir os valores em cada função
def organizarValores(valores):

    if len(valores) == 0:
        print('='*60) 
        print("Nenhum valor fornecido.")
        return
    
    print('='*60)
    
    # atribuindo os valores ás respectivas equações
    media = calcular_media(valores)
    maior = calcular_maior(valores)
    menor = calcular_menor(valores)
    soma = calcular_soma(valores)
    
    # interface
    print(f"Valores: {valores}")
    print(f"Média: {media:.2f}")
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
    print(f"Soma dos valores: {soma}")
    
    print('='*60)


def main():
    valores = receber_valores()
    organizarValores(valores)


main()
print('fim do programa, gg')
