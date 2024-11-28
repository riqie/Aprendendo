from graphAL import GraphAL


# Exemplo de uso
grafo = GraphAL()
grafo.add_vertex('a')
grafo.add_vertex('b')
grafo.add_vertex('c')

grafo.add_edge('a', 'b')
grafo.add_edge('a', 'c')
grafo.add_edge('b', 'c')

grafo.print_graph()

grafo.remove_vertex('b')

grafo.print_graph()

