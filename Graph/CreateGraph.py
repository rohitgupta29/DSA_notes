class Graph:
    def __init__(self, matrix):
        # Initialize the number of vertices based on the length of the adjacency matrix
        self.num_vertices = len(matrix)
        # Create an adjacency list to store the graph
        # Each vertex will have a list of its adjacent vertices
        self.adjacency_list = [[] for _ in range(self.num_vertices)]

        # Populate the adjacency list from the adjacency matrix
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                # If there is an edge between vertex i and vertex j (non-zero value)
                if matrix[i][j] != 0:
                    # Add vertex j to the adjacency list of vertex i
                    self.adjacency_list[i].append(j)
                    # print("adj_list: ",self.adjacency_list)

    def add_edge(self, source, destination):
        # Add a directed edge from the source vertex to the destination vertex
        self.adjacency_list[source].append(destination)

    def remove_edge(self, source, destination):
        # Remove the edge from the source vertex to the destination vertex
        self.adjacency_list[source].remove(destination)

    def print_graph(self):
        # Print the adjacency list representation of the graph
        for i in range(self.num_vertices):
            # Print the current vertex
            print(f"Vertex {i}: ", end="")
            # Print all neighbors of the current vertex
            for neighbor in self.adjacency_list[i]:
                print(f"-> {neighbor} ", end="")
            print()  # Print a new line after each vertex

# Example usage
matrix = [
    [0, 1, 0, 1],  # Vertex 0 is connected to Vertex 1 and Vertex 3
    [1, 0, 1, 0],  # Vertex 1 is connected to Vertex 0 and Vertex 2
    [0, 1, 0, 1],  # Vertex 2 is connected to Vertex 1 and Vertex 3
    [1, 0, 1, 0]   # Vertex 3 is connected to Vertex 0 and Vertex 2
]

# Create a graph using the adjacency matrix
graph = Graph(matrix)
# Print the adjacency list representation of the graph
graph.print_graph()
