from graphAM import GraphAM


g = GraphAM()
g.add_vertex('A')
g.add_vertex('B')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.print_graph()
