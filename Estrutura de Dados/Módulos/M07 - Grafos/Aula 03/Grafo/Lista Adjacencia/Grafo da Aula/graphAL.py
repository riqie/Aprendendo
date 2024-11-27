class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class GraphAL:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Adiciona arestas
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

class GraphAL:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    def print_graph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ";", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print("\n")
