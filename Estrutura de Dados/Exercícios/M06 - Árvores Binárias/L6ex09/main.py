'''9. Crie uma árvore binária ordenada para implementar um dicionário da língua inglesa.
Cada nó precisa ter a palavra e o seu significado. Implemente as funções básicas
para inserção, remoção, pesquisa e impressão do dicionário.'''


from binaryTree import BinaryTree
from nodeTree import NodeTree

def main():
    arvore = BinaryTree()
    while True:
        print("\n\n===== MENU =====")
        print("1. Inserir palavra no dicionário")
        print("2. Buscar palavra no dicionário")
        print("3. Remover palavra do dicionário")
        print("4. Imprimir dicionário")
        print("5. Sair")
        print("================")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            word = input("Digite a palavra: ")
            meaning = input("Digite o significado: ")
            if arvore.isEmpty():
                arvore.root = NodeTree(word, meaning)
            else:
                arvore.insert(arvore.root, word, meaning)
            print(f'Palavra "{word}" inserida no dicionário.')

        elif escolha == 2:
            word = input("Digite a palavra a ser buscada: ")
            resultado = arvore.search(arvore.root, word)
            if resultado:
                print(f'{resultado.word}: {resultado.meaning}')
            else:
                print(f'Palavra "{word}" não encontrada no dicionário.')

        elif escolha == 3:
            word = input("Digite a palavra a ser removida: ")
            arvore.root = arvore.delete(arvore.root, word)
            print(f'Palavra "{word}" removida do dicionário.')

        elif escolha == 4:
            print("Dicionário em ordem alfabética:")
            arvore.printInOrder(arvore.root)

        elif escolha == 5:
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

main()
