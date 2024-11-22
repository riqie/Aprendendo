from nodeTree import NodeTree


class BinaryTree():
    def __init__(self):
        self.root = None


    def isEmpty(self):
        return self.root is None
    

    def insert(self, node, data):

        if self.isEmpty():
            self.root = NodeTree()

        else:
            if data < node.data:
                if node.left is None:
                    node.left = NodeTree(data)
                else:
                    self.insert(node.left, data)

            elif data == node.data:
                print("\nSame data is invalid.\n")

            else:
                if node.right is None: 
                    node.right = NodeTree(data)
                else:
                    self.insert(node.right, data)


    def search(self, node, data):
        
        if self.isEmpty() or node.data == data:
            return node
        
        if data < node.data:
            return self.search(node.left, data)

        else:
            return self.search(node.right, data)


    def printInOrder(self, node):
        
        if self.isEmpty():
            print("\nEmpty Tree!")

        else:
            if node.left:
                self.printInOrder(node.left)
                
            print(node.data, " ",end="")

            if node.right:
                self.printInOrder(node.rigth)


    def printPreOrder(self, node):
        
        if self.isEmpty():
            print("\nEmpty Tree!")

        else:
            print(node.data, " ",end="")

            if node.left:
                self.printInOrder(node.left)

            if node.right:
                self.printInOrder(node.rigth)


    def printPostOrder(self, node):
        
        if self.isEmpty():
            print("\nEmpty Tree!")

        else:
            if node.left:
                self.printInOrder(node.left)

            if node.right:
                self.printInOrder(node.rigth)

            print(node.data, " ",end="")

    
    def minNode(self, node):
        
        if self.isEmpty():
            print("\nEmpty Tree!")

        else:
            while node.left:
                node = node.left
                
            return node.data
    

    def maxNode(self, node):
        
        if self.isEmpty():
            print("\nEmpty Tree!")

        else:
            while node.right:
                node = node.right

            return node.data


    def heightTree(self, node):

        if node:
            return 1 + max(self.heightTree(node.left), self.heightTree(node.right))

        else:
            return 0
        
    
    def countNodes(self, node):

        if node is None:
            return 0
        
        return 1 + self.countNodes(node.left), self.countNodes(node.right)

    
    def delete(self, node, data):
        
        if node is None:
            return node

        elif data < node.data:
            node.left = self.delete(node.left, data)

        elif data > node.data:
            node.right = self.delete(node.right, data)

        else:
            if node.left is None and node.right is None:
                return None
            
            elif node.left is None:
                return node.right
            
            elif node.right is None:
                return node.left

            else:
                sucessor = self._minValueRight(node.right)
                node.data = sucessor.data
                node.right = self.delete(node.right, sucessor.data)
        
        return node

    
    def _minValueRight(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current
    

    def printTree(self, node, level):
        
        if node is not None:
            self.printTree(node.right, level + 1)
            print(" "*level + f'-> {node.data}')
            self.printTree(node.left, level + 1)

    
    def deleteTree(self):
        self.root = None

