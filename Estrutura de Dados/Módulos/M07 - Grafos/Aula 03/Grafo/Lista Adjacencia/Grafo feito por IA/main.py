from graphAL import GraphAL

# Cria um grafo
g = GraphAL()

# Adiciona vértices
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')

# Adiciona arestas
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('D', 'E')
g.add_edge('E', 'A')

# Imprime o grafo
g.print_graph()
