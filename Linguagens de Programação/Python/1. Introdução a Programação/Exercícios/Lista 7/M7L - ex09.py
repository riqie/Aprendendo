'''
Escreva um programa que lê duas notas de vários alunos e armazena tais notas em 
um dicionário, onde a aluno é o nome do aluno. A entrada de dados deve terminar 
quando for lida uma string vazia como nome. Seu programa deve também calcular a 
média do aluno e exibir o nome e a média do aluno de maior média
'''

print('='*50)
print('AVISO:')
print("Este programa armazena e irforma os nomes e as notas do aluno.")
print('Deixe em branco o espaço de nome para prosseguir.')

dic = {}
dicmedia = {}

print('='*50)
while True:    
    
    aluno = input('Nome do aluno: ')
    aluno = aluno.capitalize()

    if aluno == '':
        print('='*50)
        print('Listagem das notas:')

        break

    elif aluno.is() == False:
        print('Erro, nome inválido.')

        continue

    else:
        print('Erro, nome inválido.')

        continue

   
    print('\nInsira valores aritmétcos nas notas:')
    valor1 = float(input('nota 1: '))
    valor2 = float(input('nota 2: '))


    dic[aluno] = valor1, valor2
    media = (valor1 + valor2)/2
    dicmedia[aluno] = media

    print(f'\nAluno {aluno} teve média {media}')
    print('='*50)

maiormedia = [max(dicmedia.values())]


print(f'\nA maior média da turma foi {maiormedia[0]}, alunos que possuem esta média:')
for aluno, media in dicmedia.items():
    if media in maiormedia:
        print(f' - {aluno}')

print('='*50, ' Fim do programa ', '='*50)
