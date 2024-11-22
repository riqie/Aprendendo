'''5. Faça um programa para executar as operações abaixo em uma árvore binária.
Menu
1 – Inserir número
2 – Mostrar a altura da arvore
3 – Mostrar o nível de um nó
4 – Sair
'''

from tree import BinaryTree
from node import NodeTree

def menu():
    arvore = BinaryTree()
    while True:
        print("\n\n===== MENU =====")
        print("1. Inserir número")
        print("2. Mostrar a altura da árvore")
        print("3. Mostrar o nível de um nó")
        print("4. Sair")
        print("================")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            data = int(input("Digite o número a ser inserido: "))
            if arvore.isEmpty():
                arvore.root = NodeTree(data)
            else:
                arvore.insert(arvore.root, data)
            print(f"{data} inserido na árvore.")

        elif escolha == 2:
            print(f"Altura da árvore: {arvore.heightTree(arvore.root)}")

        elif escolha == 3:
            data = int(input("Digite o número do nó: "))
            nivel = arvore.levelNode(arvore.root, data)
            if nivel != -1:
                print(f"Nível do nó {data}: {nivel}")
            else:
                print(f"Nó {data} não encontrado na árvore.")

        elif escolha == 4:
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()

