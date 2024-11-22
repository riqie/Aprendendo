'''6. Faça um programa para executar as operações abaixo em uma árvore binária.
Menu
1 – Inserir número
2 – Mostrar se a arvore é estritamente binária
3 – Mostrar se a arvore é completa
4 – Mostrar se a arvore é cheia
5 – Sair'''


from binaryTree import BinaryTree
from nodeTree import NodeTree

def main():
    arvore = BinaryTree()
    while True:
        print("\n\n===== MENU =====")
        print("1. Inserir número")
        print("2. Mostrar se a árvore é estritamente binária")
        print("3. Mostrar se a árvore é completa")
        print("4. Mostrar se a árvore é cheia")
        print("5. Sair")
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
            if arvore.isStrictlyBinary(arvore.root):
                print("A árvore é estritamente binária.")
            else:
                print("A árvore não é estritamente binária.")

        elif escolha == 3:
            if arvore.isComplete(arvore.root):
                print("A árvore é completa.")
            else:
                print("A árvore não é completa.")

        elif escolha == 4:
            if arvore.isFull(arvore.root):
                print("A árvore é cheia.")
            else:
                print("A árvore não é cheia.")

        elif escolha == 5:
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()
