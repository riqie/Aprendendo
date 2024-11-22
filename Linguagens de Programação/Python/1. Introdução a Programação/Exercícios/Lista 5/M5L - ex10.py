'''
Faça um programa para corrigir uma prova de múltipla escolha de 10 questões, cujo gabarito é b, c, d, a, a, e, b, d, a, c. Cada questão vale 1,0 ponto e a nota será de 0,0 a 10,0. O programa deve ler do teclado o número de matrícula de até 30 alunos em um vetor e suas respectivas respostas em uma matriz (que devem obrigatoriamente estar entre ‘a’ e ‘e’. A seguir, o programa deve calcular e imprimir: 
a. Para cada aluno, seu número e nota. 
b. A porcentagem de alunos aprovados, sendo a menor nota para aprovação 
igual a 6,0
'''

matriculas = []  # Vetor que armazena os numeros de matrícula
aluno = []  # Vetor que armazena as respostas de cada aluno temporariamente
turma = []  # Matriz que armazena as respostas de todos os alunos
notas = []  # Vetor que armazena as notas dos alunos
gabarito = ['b', 'c', 'd', 'a', 'a', 'e', 'b', 'd', 'a', 'c']

i = aprovados = 0

while True:
    n = int(input("Número de alunos da turma(máximo de 30): "))

    if n > 0 and n <= 30:
        break
    else:
        print('Número invalido')

while i <= n:
    j = 1  # Contador de respostas válidas pra cada questão
    print('-'*40)
    num_matricula = int(input('Informe seu número de matrícula:'))
    print('-'*40)

    if num_matricula >= 1:
        matriculas.append(num_matricula)
        print((f"ALUNO N° DE MATRÍCULA {num_matricula}").center(40))
        print(40*"-")

        while j <= 10:
            alternativas = ['a', 'b', 'c', 'd', 'e']
            resposta = str(input(f'Resposta da questão {j}:')).lower()

            if resposta in alternativas:
                aluno.append(resposta)
                j = j + 1

            else:
                print('Resposta inválida!')

        # Adiciona uma copia das respostas do aluno na lista turma
        turma.append(aluno[:])
        aluno.clear()  # Limpa a lista aluno, pra poder armazenar as respostas do prox aluno

        i = i + 1  # Contador de alunos adicionados a lista turma

    else:
        print("N° de matrícula inválido!")
        continue

    if i == n:
        break

for prova in turma:
    nota = 0
    for c in range(10):
        if prova[c] == gabarito[c]:
            nota += 1
    if nota >= 6:
        aprovados = aprovados + 1
    notas.append(nota)

for k in range(len(matriculas)):
    print('-'*40)
    print(f'Número de matrícula = {matriculas[k]}\nNota = {notas[k]:.1f}')
    print('-'*40)

print(f'Número de aprovados = {aprovados} ({
      100*aprovados/len(matriculas):.1f}% da turma)')
print('-'*40)
