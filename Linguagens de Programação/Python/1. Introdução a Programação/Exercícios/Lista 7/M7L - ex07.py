'''
Faça um programa que leia nomes de alunos e suas respectivas notas até que o
nome 'oooo' seja informado. Após o fim da leitura, exiba o nome do aluno que possui
a maior nota. Obs.: Use dicionário para resolver essa questão.

'''

ranking = {}
melhores_alunos = {}
cont = 0

while True:
    nome = input("Entre com o nome do aluno (digite 'oooo' para terminar): ")
    
    if nome == "oooo":
        break
    
    nota = float(input(f"Entre com a nota do aluno {nome}: "))
    ranking[nome] = nota

melhor_aluno = max(ranking, key=ranking.get)
melhor_nota = ranking[melhor_aluno]

for nome, nota in ranking.items():
    if nota == melhor_nota:
        cont += 1
        melhores_alunos[nome] = nota
        
if cont > 1:
    print("Os alunos com maior nota são: ")
else:
    print("O aluno com a maior nota foi o/a ", end='')

for nome, nota in melhores_alunos.items():
    print(f"{nome} com Nota {nota}!")

print(melhor_aluno)
