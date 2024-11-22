from nodeTree import NodeTree

class BinaryTree():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def insert(self, node, word, meaning):
        if self.isEmpty():
            self.root = NodeTree(word, meaning)
        else:
            if word < node.word:
                if node.left is None:
                    node.left = NodeTree(word, meaning)
                else:
                    self.insert(node.left, word, meaning)
            elif word == node.word:
                print("\nA palavra já existe no dicionário.\n")
            else:
                if node.right is None:
                    node.right = NodeTree(word, meaning)
                else:
                    self.insert(node.right, word, meaning)

    def search(self, node, word):
        if node is None or node.word == word:
            return node

        if word < node.word:
            return self.search(node.left, word)

        return self.search(node.right, word)

    def delete(self, node, word):
        if node is None:
            return node

        if word < node.word:
            node.left = self.delete(node.left, word)
        elif word > node.word:
            node.right = self.delete(node.right, word)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._minValueRight(node.right)
            node.word = temp.word
            node.meaning = temp.meaning
            node.right = self.delete(node.right, temp.word)

        return node

    def _minValueRight(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def printInOrder(self, node):
        if node is not None:
            self.printInOrder(node.left)
            print(f"{node.word}: {node.meaning}")
            self.printInOrder(node.right)
