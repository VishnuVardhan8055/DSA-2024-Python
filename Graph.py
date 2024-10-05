class Graph:
    def __init__(self):
        # Initialize an empty graph using a dictionary
        self.graph = {}

    def add_edge(self, u, v):
        # Add an edge from vertex u to vertex v
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

        # If the graph is undirected, uncomment the following lines
        # if v not in self.graph:
        #     self.graph[v] = []
        # self.graph[v].append(u)

    def remove_edge(self, u, v):
        # Remove the edge from vertex u to vertex v
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)

        # If the graph is undirected, uncomment the following lines
        # if v in self.graph and u in self.graph[v]:
        #     self.graph[v].remove(u)

    def display(self):
        # Display the graph
        for vertex in self.graph:
            print(f"{vertex}: {', '.join(map(str, self.graph[vertex]))}")

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')

    print("Graph adjacency list:")
    g.display()

    g.remove_edge('A', 'C')
    print("\nGraph after removing edge A -> C:")
    g.display()
