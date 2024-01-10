import itertools 

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
        

def BruteForceTSP(graph):
    vertex = []
    for i in range(graph.V):
        if i != 0:
            vertex.append(i)
    min_path = 999999999
    next_permutation = itertools.permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = i[0]
        for j in i:
            current_pathweight += graph.graph[k][j]
            k = j
        current_pathweight += graph.graph[k][0]
        min_path = min(min_path, current_pathweight)
    return min_path

if __name__ == "__main__":
    v = 4
    g = Graph(v)
    g.graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    print(BruteForceTSP(g))
