'''
Faça um editor de texto usando uma matriz, que forneça as seguintes funções:
    a. O texto do usuário deve ser lido até que uma linha em branco seja digitada.
    b. O usuário pode reimprimir seu texto digitando i.
    c. O usuário pode trocar duas linhas de lugar digitando t onde o editor pergunta
       os números das linhas a serem trocadas entre si.
    d. O usuário pode redigitar uma linha digitando r, onde o editor pergunta o
       número da linha a ser redigitada.
    e. O usuário pode sair do editor digitando s.
    f. Se o usuário digitar um comando que não se encaixe em nenhum caso acima,
       o editor avisa que o comando não existe. 
'''

matriz_texto = []
entrada = "a"

print('-'*100)
print("\tEntre com o seu texto. Digite Enter em um espaço em brancos para terminar.")
while True:
    linha = input()
    if linha == "":
        break
    matriz_texto.append(linha)
texto = "\n".join(matriz_texto)

#print (matriz_texto)
print('-'*40)
print("\t SEU TEXTO:")
print (texto)

while entrada != "s" :
    print('-'*40)
    print("\tFunções do Editor de Texto")
    print("i -> Reimprime o texto")
    print("t -> Troca uma linha por outra")
    print("r -> Redigitar uma linha do texto")
    print("s -> Sair do editor")
    entrada = input("Escolha uma opção: ")
    print('-'*40)

    if entrada == "i":
        print(texto)

    elif entrada == "t":
        l1 = int(input("Digite o número da primeira linha: "))
        l2 = int(input("Digite o número da segunda linha: "))
        print('-'*40)
        if 0 < l1 <= len(matriz_texto) and 0 < l2 <= len(matriz_texto):
            matriz_texto[l1-1],matriz_texto[l2-1] = matriz_texto[l2-1],matriz_texto[l1-1] #troca das linhas
            texto = "\n".join(matriz_texto) #transformando matriz em texto
            print (texto)
        else:
            print("Linha fornecida inválida.")

    elif entrada == "r":
        l1 = int(input("Qual linha você deseja redigitar? "))
        if 0 < l1 <= len(matriz_texto):
            linha = input("Escreva a nova linha:")
            print('-'*40)
            matriz_texto.insert(l1-1, linha)
            matriz_texto.pop(l1)
            texto = "\n".join(matriz_texto)
            print(texto)
        else:
            print("Linha fornecida inválida")
        

    elif entrada == "s":
        pass

    else:
        print("O comando digitado não existe.")

print("Obrigado por usar!")
