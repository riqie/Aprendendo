class GraphAM:
    """
    Uma classe para representar um grafo usando uma matriz de adjacência.
    """

    def __init__(self):
        """
        Inicializa o grafo com uma matriz de adjacência vazia e uma lista de vértices.
        """
        self.__n = 0
        self.__g = []
        self.__listOfVertex = []

    def __resize_matrix(self):
        """
        Redimensiona a matriz de adjacência quando um novo vértice é adicionado.
        A matriz é expandida para acomodar os novos vértices.
        """
        size = len(self.__listOfVertex)

        while len(self.__g) < size:
            self.__g.append([0] * size)

        for row in self.__g:
            while len(row) < size:
                row.append(0)

    def add_vertex(self, vertex):
        """
        Adiciona um vértice ao grafo.
        
        :param vertex: O vértice a ser adicionado ao grafo.
        """
        if vertex not in self.__listOfVertex:
            self.__listOfVertex.append(vertex)
            self.__n = len(self.__listOfVertex)
            self.__resize_matrix()

    def add_edge(self, source, destination):
        """
        Adiciona uma aresta entre dois vértices no grafo.
        
        :param source: O vértice de origem.
        :param destination: O vértice de destino.
        """
        # Verifica e adiciona os vértices, se necessário
        self.add_vertex(source)
        self.add_vertex(destination)

        # Obtém os índices dos vértices
        indexS = self.__listOfVertex.index(source)
        indexD = self.__listOfVertex.index(destination)
        
        # Adiciona a aresta na matriz de adjacência
        self.__g[indexS][indexD] = 1
        self.__g[indexD][indexS] = 1  # Para grafos não direcionados

    def remove_vertex(self, vertex):
        """
        Remove um vértice do grafo.
        
        :param vertex: O vértice a ser removido.
        """
        if vertex in self.__listOfVertex:
            index = self.__listOfVertex.index(vertex)
            self.__listOfVertex.remove(vertex)
            self.__g.pop(index)

            for row in self.__g:
                row.pop(index)
            self.__n = len(self.__listOfVertex)
        else:
            print(f"O vértice {vertex} não existe no grafo.")

    def print_graph(self):
        """
        Imprime a matriz de adjacência do grafo.
        """
        print("\nVértices: ", end="")
        for vertex in self.__listOfVertex:
            print(f"\t{vertex}", end="")

        print("\n\nMatriz de Adjacência:")
        for i in range(self.__n):
            print(f"{self.__listOfVertex[i]}", end=" ")

            for j in range(self.__n):
                print(f"\t{self.__g[i][j]}", end="")
            print()
        print()
