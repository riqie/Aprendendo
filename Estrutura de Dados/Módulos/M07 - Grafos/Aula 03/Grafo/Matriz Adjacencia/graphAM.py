

class GraphAM:
    # no of vertices
    __n = 0
    #adjacency matrix of size 10x10 initialize with 0
    __g = [[0 for column in range(10) for row in range(10)]]
    __listOfVertex = []

    def __init__(self, vertex):
        #adding a vertex in a list
        self.__listOfVertex.append(vertex)
        #saving no of vertices
        self.__n = len(self.__)