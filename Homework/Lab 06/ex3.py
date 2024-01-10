class Graph:
    def __init__(self, vertices, edges):
        self.V = vertices
        self.E = edges
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)] for row in range(vertices)]
        
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
        self.graph_matrix[u][v] = w
        self.graph_matrix[v][u] = w

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph_matrix[i][ parent[i] ])
            
    def minKey(self, key, mstSet):
        min = float('inf')
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index
    
    def primMST(self):
        key = [float('inf')] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph_matrix[u][v] > 0 and mstSet[v] == False and key[v] > self.graph_matrix[u][v]:
                    key[v] = self.graph_matrix[u][v]
                    parent[v] = u
        self.printMST(parent)
        
g = Graph(5, 7)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)
g.primMST()

# Basic OP: assignment in line 37
# Worst case: O(n^2)
# T(n)  = T(n-1) + O(n) = O(n^2)
# Time complexity: O(n^2)