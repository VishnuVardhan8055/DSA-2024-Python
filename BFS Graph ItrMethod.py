class Graph:

    def __init__(self):
        self.graph = {}

    def addedge(self,Edge,Vertices):

        if Edge not in self.graph:
            self.graph[Edge] = []

        if Vertices not in self.graph:
            self.graph[Vertices] = []
        self.graph[Edge].append(Vertices)

    def BFS(self, start):
        visited = set()
        queue = [start]

        while queue:
            cur = queue.pop(0)
            if cur not in visited:
                print(cur,'-->', end=' ')
                visited.add(cur)
                for val in self.graph[cur]:
                    if val not in visited:
                        queue.append(val)

    def Disply(self):
        for vertices in self.graph:

            print(f"{vertices}: {', '.join(map(str, self.graph[vertices]))}")


G = Graph()

G.addedge('A','B')
G.addedge('A','C')
G.addedge('C','E')
G.addedge('E','F')
G.addedge('B','D')
G.addedge('D','F')
G.addedge('B','F')

G.Disply()


print()


start = 'A'
G.BFS(start)