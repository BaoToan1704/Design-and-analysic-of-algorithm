class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, reach):
        print("Following matrix transitive closure of the given graph")
        for i in range(self.V):
            for j in range(self.V):
                print("%d" % reach[i][j], end=' ')
            print("")
        print("")
        return

def Warshall(graph):
    reach = [[0 for i in range(graph.V)] for j in range(graph.V)]
    for i in range(graph.V):
        for j in range(graph.V):
            reach[i][j] = graph.graph[i][j]
    for k in range(graph.V):
        for i in range(graph.V):
            for j in range(graph.V):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    graph.printSolution(reach)
    
if __name__ == "__main__":
    g = Graph(4)
    g.graph = [[0, 1, 0, 1],
               [0, 0, 1, 0],
               [0, 0, 0, 1],
               [0, 0, 0, 0]]
    Warshall(g)

