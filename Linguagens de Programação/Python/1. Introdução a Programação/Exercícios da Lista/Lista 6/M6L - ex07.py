'''
Defina uma matriz de caracteres para guardar um texto para fazer um editor de texto
que leia as várias linhas dadas pelo usuário e quando este digitar uma linha em
branco, reescreva o texto do usuário e imprima as seguintes estatísticas do texto:
número de caracteres digitados, número de espaços em branco e número de linhas.

'''

matriz_texto = []
qntdCaracteres = 0
qntdEspaco = 0
print("-"*80)
print ("\tDigite um texto. Pressione Enter em uma linha em branco para terminar.")

while True:
    linha = input()
    if linha == "":
        break
    matriz_texto.append(linha)
texto = "\n".join(matriz_texto)

print('-'*40)
print("\t SEU TEXTO:")
print (texto)
print('-'*40)

for linha in matriz_texto:
    qntdCaracteres += len(linha)
    qntdEspaco += linha.count(' ')

print(f"Caracteres: {qntdCaracteres}")
print(f"Espaços em branco: {qntdEspaco}")
print(f"Linhas: {len(matriz_texto)}")
