from binaryTree import BinaryTree
from nodeTree import NodeTree

def menu():
    arvore = BinaryTree()
    
    while True:
        print("\n\n===== MENU =====")
        print("1. Inserir número na árvore")
        print("2. Buscar um nó na árvore")
        print("3. Imprimir em ordem")
        print("4. Imprimir em pré-ordem")
        print("5. Imprimir em pós-ordem")
        print("6. Encontrar o nó mínimo")
        print("7. Encontrar o nó máximo")
        print("8. Altura da árvore")
        print("9. Contar nós")
        print("10. Deletar um nó")
        print("11. Deletar toda a árvore")
        print("0. Sair")
        print("================")

        escolha = int(input("\nEscolha uma opção: "))

        if escolha == 1:
            data = int(input("\nDigite o número a ser inserido: "))
            if arvore.isEmpty():
                arvore.root = NodeTree(data)
            else:
                arvore.insert(arvore.root, data)
            print(f"{data} inserido na árvore.")

        elif escolha == 2:
            data = int(input("\nDigite o número a ser buscado: "))
            resultado = arvore.search(arvore.root, data)
            if resultado:
                print(f"Nó com valor {data} encontrado.")
            else:
                print(f"Nó com valor {data} não encontrado.")

        elif escolha == 3:
            print("\nImpressão em ordem:")
            arvore.printInOrder(arvore.root)

        elif escolha == 4:
            print("\nImpressão em pré-ordem:")
            arvore.printPreOrder(arvore.root)

        elif escolha == 5:
            print("\nImpressão em pós-ordem:")
            arvore.printPostOrder(arvore.root)

        elif escolha == 6:
            if arvore.isEmpty():
                print("\nÁrvore vazia!")
            else:
                print(f"\nNó mínimo: {arvore.minNode(arvore.root)}")

        elif escolha == 7:
            if arvore.isEmpty():
                print("\nÁrvore vazia!")
            else:
                print(f"\nNó máximo: {arvore.maxNode(arvore.root)}")

        elif escolha == 8:
            print(f"\nAltura da árvore: {arvore.heightTree(arvore.root)}")

        elif escolha == 9:
            print(f"\nTotal de nós: {arvore.countNodes(arvore.root)}")

        elif escolha == 10:
            data = int(input("\nDigite o número a ser deletado: "))
            arvore.root = arvore.delete(arvore.root, data)
            print(f"\nNó com valor {data} deletado.")

        elif escolha == 11:
            arvore.deleteTree()
            print("\nÁrvore deletada.")

        elif escolha == 0:
            print("\nSaindo...")
            break

        else:
            print("\nOpção inválida. Tente novamente.")

def main():
    menu()

main()
