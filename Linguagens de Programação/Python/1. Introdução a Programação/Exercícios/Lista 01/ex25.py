# Foi realizada uma pesquisa de algumas características físicas da população de uma
# certa região, a qual foram coletados os seguintes dados referentes a cada habitante
# para serem analisados:
# • Sexo.
# • Cor dos olhos (azuis, verdes, castanhos).
# • Cor dos cabelos (louros, castanhos, pretos).
# • Idade.
# Faça um programa que determine e escreva:
# a. O total de entrevistados
# b. O total de homens e o total de mulheres entrevistados
# c. A maior e a menor idade do conjunto de habitantes;
# d. A média de idade do conjunto de habitantes;
# e. A percentagem de indivíduos de sexo feminino cuja idade está entre 18 e 35
# anos inclusive e que tenham olhos verdes e cabelos louros.
# O final do conjunto de habitantes é reconhecido pelo valor -1 para a idade.

def dadosColetados():
    listaDados = []

    sexo = input()
    corOlhos = input()
    corCabelo = input()
    idade = input()

    listaDados.append(dados = {
    'Sexo' : sexo,
    'Olhos' : corOlhos,
    'Cabelo': corCabelo,
    'Idade' : idade
    })
    

    return listaDados

def main():
    print('') #colocar enunciado
    contador = 1
    while True:
        listaDados = dadosColetados()

        contador = input('Deseja continuar?\nPressione qualquer tecla para continuar, digite "0" para sair.')
        if contador == 0:
            print('fim')
            break
    
    totalEntrevistados = len(listaDados)

    totalHomens = 0 
    totalMulheres = 0

    for dicionario_dados in listaDados:
        for valor in dicionario_dados.values():

            if valor.value == 'masculino':
                totalHomens += 1

            elif valor.value == 'feminino':
                totalMulheres += 1
                   

                





    maiorIdade = 
    menorIdade = 
    mediaIdade = 

    mulheres_idade_olhos_cabelos =
        


























