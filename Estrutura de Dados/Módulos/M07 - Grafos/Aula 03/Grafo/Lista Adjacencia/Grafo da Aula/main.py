from graphAL import GraphAL

V = 5

g1 = GraphAL(V)
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(0, 3)
g1.add_edge(1, 2)
g1.print_graph()
