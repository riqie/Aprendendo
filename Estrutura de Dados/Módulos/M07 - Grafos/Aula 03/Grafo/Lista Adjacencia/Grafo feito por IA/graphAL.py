class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent = []

    def add_edge(self, neighbor):
        self.adjacent.append(neighbor)

    def remove_edge(self, neighbor):
        self.adjacent.remove(neighbor)


class GraphAL:
    def __init__(self):
        self.nodes = {}

    def add_vertex(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, source, destination):
        if source not in self.nodes:
            self.add_vertex(source)
        if destination not in self.nodes:
            self.add_vertex(destination)

        self.nodes[source].add_edge(destination)
        self.nodes[destination].add_edge(source)  # Para grafos não direcionados

    def remove_vertex(self, value):
        if value in self.nodes:
            for neighbor in self.nodes[value].adjacent:
                self.nodes[neighbor].remove_edge(value)
            del self.nodes[value]

    def print_graph(self):
        for node in self.nodes.values():
            print(f"{node.value}: {node.adjacent}")
