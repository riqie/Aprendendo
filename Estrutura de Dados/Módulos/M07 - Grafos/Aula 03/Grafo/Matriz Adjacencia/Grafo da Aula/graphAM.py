

class GraphAM:
    __n = 0 # numero de vertices
    
    # --------------------------------------------
    # matriz adjacente 10x10, possuindo apenas zeros. 
    __g = [] 

    for row in range(10):
        line = []

        for column in range(10):
            line.append(0)

        __g.append(line)

    __listOfVertex = []
    # --------------------------------------------

    def __init__(self, vertex):
        # adicionando um vertice na lista
        self.__listOfVertex.append(vertex)
        # salvando numero de vertices  
        self.__n = len(self.__listOfVertex)
        # atualizando a matriz
        for source in range(0, self.__n):
            for destination in range(0, self.__n):
                self.__g[source][destination] = 0


    def add_vertex(self, source, destination):
        # Inicializa o índice da origem e do destino como 0
        indexS = indexD = 0

        # Verifica e adiciona o vértice de origem
        if source not in self.__listOfVertex:
            print("Vertex {0} not present in Graph, adding it automatically.".format(source))
            self.__listOfVertex.append(source)
        indexS = self.__listOfVertex.index(source)

        # Verifica e adiciona o vértice de destino
        if destination not in self.__listOfVertex:
            print("Vertex {0} not present in Graph, adding it automatically.".format(destination))
            self.__listOfVertex.append(destination)
        indexD = self.__listOfVertex.index(destination)

        self.__n = len(self.__listOfVertex)

        # Atualiza a matriz para incluir novos vértices
        if (indexS >= self.__n) or (indexD >= self.__n):
            print("One of the vertex doesn't exist!")

        if self.__n > 1:
            for i in range(self.__n):
                self.__g[i][self.__n - 1] = 0
                self.__g[self.__n - 1][i] = 0


    def add_edge(self, source, destination):
        # Inicializa o índice de origem e de destino com 0
        indexS = 0
        indexD = 0

        # Verifica se o vértice de origem está na lista __listOfVertex
        if source in self.__listOfVertex:
            # Obtém o índice do vértice de origem na lista
            indexS = self.__listOfVertex.index(source)
        else:
            # Imprime uma mensagem indicando que o vértice não pode ser incluído e sugere adicioná-lo
            print('Cannot be included in the graph, Add the vertex {0}'.format(source))

        # Verifica se o vértice de destino está na lista __listOfVertex
        if destination in self.__listOfVertex:
            # Obtém o índice do vértice de destino na lista
            indexD = self.__listOfVertex.index(destination)
        else:
            # Imprime uma mensagem indicando que o vértice não pode ser incluído e sugere adicioná-lo
            print('Cannot be included in the graph, Add the vertex {0}'.format(destination))

        # Verifica se os índices de origem ou destino são maiores ou iguais ao número total de vértices
        if (indexS >= self.__n) or (indexD >= self.__n):
            # Imprime uma mensagem informando que um dos vértices não existe
            print("One of the vertex doesn't exist!")

        # Se o número total de vértices for maior que 1
        if self.__n > 1:
            # Itera sobre o número total de vértices
            for i in range(0, self.__n):
                # Inicializa as ligações da nova linha e coluna na matriz de adjacência com 0
                self.__g[i][self.__n-1] = 0
                self.__g[self.__n-1][i] = 0

        if destination in self.__listOfVertex:
            indexD = self.__listOfVertex.index(destination)
        else:
            print("Cannot be included in the graph, Add the vertex {0}".format(destination))

        if (indexS > 0 and indexS == indexD):
            print("Same Source and Destination")
        else:
            self.__g[indexS][indexD] = 1
            self.__g[indexD][indexS] = 1


    def removeVertex(self, location):
        # Inicializa o índice de localização como 0
        indexL = 0
        
        # Verifica se o vértice está na lista de vértices
        if location in self.__listOfVertex:
            # Obtém o índice do vértice na lista
            indexL = self.__listOfVertex.index(location)
            
            # Loop para ajustar a matriz de adjacência
            while indexL < self.__n:
                # Itera sobre todos os vértices para ajustar as colunas
                for i in range(0, self.__n):
                    self.__g[i][indexL] = self.__g[i][indexL + 1]
                
                # Itera sobre todos os vértices para ajustar as linhas
                for i in range(0, self.__n):
                    self.__g[indexL][i] = self.__g[indexL + 1][i]
                
                # Incrementa o índice de localização
                indexL = indexL + 1
            
            # Decrementa o número total de vértices
            self.__n = self.__n - 1
            
            # Remove o vértice da lista de vértices
            self.__listOfVertex.remove(location)
            
            # Imprime mensagem de sucesso
            print("Successfully removed {0} from graph; current list of vertex are below:\n {1}".format(location, self.__listOfVertex))
        else:
            # Imprime mensagem de erro se o vértice não existir
            print("No such vertex exist in the graph")


    def print_graph(self):
        # Imprime uma linha em branco
        print("\n")
        
        # Loop para imprimir os vértices
        for i in range(len(self.__listOfVertex)):
            # Imprime um vértice com uma tabulação e sem nova linha
            print("\t", self.__listOfVertex[i], end="")
        
        # Loop para imprimir a matriz de adjacência
        for i in range(0, self.__n):
            # Imprime uma nova linha com o vértice correspondente
            print("\n", self.__listOfVertex[i], end=" ")
            for j in range(0, self.__n):
                # Imprime o valor da matriz de adjacência com tabulação e sem nova linha
                print("\t", self.__g[i][j], end="")
        
        # Imprime uma nova linha
        print("\n")
