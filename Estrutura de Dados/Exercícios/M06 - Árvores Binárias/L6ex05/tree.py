from node import NodeTree


class BinaryTree():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def insert(self, node, data):
        if self.isEmpty():
            self.root = NodeTree(data)
        else:
            if data < node.data:
                if node.left is None:
                    node.left = NodeTree(data)
                else:
                    self.insert(node.left, data)
            elif data == node.data:
                print("\nMesmo valor é inválido.\n")
            else:
                if node.right is None:
                    node.right = NodeTree(data)
                else:
                    self.insert(node.right, data)

    def heightTree(self, node):
        if node:
            return 1 + max(self.heightTree(node.left), self.heightTree(node.right))
        else:
            return 0

    def levelNode(self, node, data, level=1):
        if node is None:
            return -1
        if node.data == data:
            return level
        downlevel = self.levelNode(node.left, data, level + 1)
        if downlevel != -1:
            return downlevel
        downlevel = self.levelNode(node.right, data, level + 1)
        return downlevel
