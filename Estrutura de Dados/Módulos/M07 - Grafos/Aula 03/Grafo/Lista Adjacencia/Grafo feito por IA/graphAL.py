class GraphAL:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []


    def add_edge(self, source, destination):
        if source not in self.adj_list:
            self.add_vertex(source)
        if destination not in self.adj_list:
            self.add_vertex(destination)

        self.adj_list[source].append(destination)
        self.adj_list[destination].append(source)  # Para grafos não direcionados


    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for neighbor in self.adj_list[vertex]:
                self.adj_list[neighbor].remove(vertex)

            del self.adj_list[vertex]


    def print_graph(self):
        for vertex, edges in self.adj_list.items():
            print(f"{vertex}: {edges}")
