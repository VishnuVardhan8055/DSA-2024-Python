class Graph:

    def __init__(self):
        self.graph = {}

    def addedge(self,Edge,Vertices):

        if Edge not in self.graph:
            self.graph[Edge] = []

        if Vertices not in self.graph:
            self.graph[Vertices] = []
        self.graph[Edge].append(Vertices)

    def DFS(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, '-->', end=' ')

        for val in self.graph[start]:
            if val not in visited:
                self.DFS(val, visited)

    def Display(self):
        for vertices in self.graph:

            print(f"{vertices}: {', '.join(map(str, self.graph[vertices]))}")



    def remove_edge(self, u, v):
        # Remove the edge from vertex u to vertex v
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)

G = Graph()

G.addedge('A','B')
G.addedge('A','C')
G.addedge('C','E')
G.addedge('E','F')
G.addedge('B','D')
G.addedge('D','F')
G.addedge('B','F')

G.Display()


print()


start = 'A'
G.DFS(start)


G.remove_edge('A', 'C')
print("\nGraph after removing edge A -> C:")
G.Display()