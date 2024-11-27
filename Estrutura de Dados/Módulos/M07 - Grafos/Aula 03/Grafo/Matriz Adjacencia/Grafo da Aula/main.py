# Importa a classe GraphAM do módulo graphAM
from graphAM import GraphAM

# Cria uma instância do grafo g1 com o vértice inicial "A"
g1 = GraphAM("A")

# Adiciona vértices e arestas no grafo g1
g1.add_vertex("A", "B")
g1.add_vertex("B", "C")
g1.add_vertex("D", "E")
g1.add_vertex("F", "G")
g1.add_vertex("D", "G")

g1.add_edge("A", "B")
g1.add_edge("B", "C")
g1.add_edge("D", "E")
g1.add_edge("F", "G")
g1.add_edge("D", "G")

# Imprime o grafo
g1.print_graph()

# Remove o vértice "C" e imprime o grafo novamente
g1.removeVertex("C")
g1.print_graph()
