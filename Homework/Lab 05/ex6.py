# Topological Sorting
# 1) Perform DFS traversal, noting the order vertices are popped off the traversal stack
# 2) Reverse order solves topological sorting problem

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}
        self.marked = {}
        self.count = 0
        self.stack = []

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

    def dfs(self, vertex):
        self.marked[vertex] = 1
        self.count += 1
        print(vertex, self.count)
        for w in self.edges[vertex]:
            if self.marked[w] == 0:
                self.dfs(w)
        self.stack.append(vertex)

    def dfs_traversal(self):
        for v in self.vertices:
            if self.marked[v] == 0:
                self.dfs(v)

    def topological_sort(self):
        self.dfs_traversal()
        print(self.stack)
        self.stack.reverse()
        print(self.stack)

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
g.topological_sort()
    