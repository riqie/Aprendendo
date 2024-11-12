'''
Exercício 2.
Escreva um programa que recebe como entrada um número inteiro n. Em seguida, 
seu programa deve receber as informações de n pessoas (nome, CPF e idade). Para 
cada pessoa seu programa deve armazenar as informações utilizando uma estrutura 
de dicionário. Infelizmente, algumas entradas do cadastro podem estar repetidas e 
você deve removê-las (utilize a chave CPF para isso). No fim, seu programa deve 
imprimir a lista de pessoas, sem repetições. Ao remover as repetições mantenha 
sempre o primeiro registro lido da pessoa.

Exemplo de entrada:
José 999.999.999-99 19
Maria 888.888.888-88 18
José 999.999.999-99 20
Bob 777.777.777-77 21
Josué 999.999.999-99 20
Bob 777.777.777-77 20

Resposta:
José 999.999.999-99 19
Maria 888.888.888-88 18
Bob 777.777.777-77 21
'''

pessoas = {}

n = int(input("Quantas pessoas terão no cadastro?"))

for c in range(n):
    
    print(33*"-")
    nome = str(input("NOME = "))
    cpf = int(input("CPF = "))
    idade = int(input("IDADE = "))

    if cpf not in pessoas:
        pessoas[cpf] = {'nome': nome, 'idade': idade}

print(33*"-")
print()
print(37*"-")
print(f"{('LISTA DE PESSOAS'):^37}")     
print(37*"-")
Nome = "NOME"
Cpf = "CPF" 
Idade = "IDADE"
print(f"{Nome:14}{Cpf:18}{Idade:>5}")

for chave, valor in pessoas.items():
    chave = str(chave)
    print(37*"-")
    print(f"{valor['nome']:14}",end='')
    print(f"{(chave[0:3] + '.' + chave[3:6] + '.' + chave[6:9] + '-' + chave[9:11]):18}",end='')
    print(f"{idade:<5}")

print(37*"-")


 
   





