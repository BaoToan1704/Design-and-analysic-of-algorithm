# Breadth first search

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}
        self.marked = {}
        self.count = 0

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = vertex
            self.marked[vertex] = 0

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.vertices:
            self.add_vertex(vertex1)
        if vertex2 not in self.vertices:
            self.add_vertex(vertex2)
        if vertex1 not in self.edges:
            self.edges[vertex1] = []
        if vertex2 not in self.edges:
            self.edges[vertex2] = []
        self.edges[vertex1].append(vertex2)
        self.edges[vertex2].append(vertex1)

    def bfs(self, vertex):
        queue = []
        self.marked[vertex] = 1
        self.count += 1
        print(vertex, self.count)
        queue.append(vertex)
        while len(queue) > 0:
            v = queue.pop(0)
            for w in self.edges[v]:
                if self.marked[w] == 0:
                    self.marked[w] = 1
                    self.count += 1
                    print(w, self.count)
                    queue.append(w)

    def bfs_traversal(self):
        for v in self.vertices:
            if self.marked[v] == 0:
                self.bfs(v)
                
# Driver code
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(3, 7)
g.add_edge(4, 8)
g.add_edge(4, 9)
g.bfs_traversal()