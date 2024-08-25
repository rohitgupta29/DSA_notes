class Graph:
    def __init__(self, matrix):
        # Initialize the number of vertices based on the length of the adjacency matrix
        self.num_vertices = len(matrix)
        # Create an adjacency list to store the graph
        self.adjacency_list = [[] for _ in range(self.num_vertices)]

        # Populate the adjacency list from the adjacency matrix
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if matrix[i][j] != 0:  # Check for edges
                    self.adjacency_list[i].append(j)

    def add_edge(self, source, destination):
        # Add a directed edge from the source vertex to the destination vertex
        self.adjacency_list[source].append(destination)

    def remove_edge(self, source, destination):
        # Remove the edge from the source vertex to the destination vertex
        self.adjacency_list[source].remove(destination)

    def print_graph(self):
        # Print the adjacency list representation of the graph
        for i in range(self.num_vertices):
            print(f"Vertex {i}: ", end="")
            for neighbor in self.adjacency_list[i]:
                print(f"-> {neighbor} ", end="")
            print()  # Print a new line after each vertex

    def dfs_recursive(self, start_vertex):
        # Create a list to track visited vertices
        visited = [False] * self.num_vertices
        print("DFS traversal (recursive) starting from vertex", start_vertex, ":")
        self._dfs_recursive_helper(start_vertex, visited)
        print()  # Print a new line after DFS traversal

    def _dfs_recursive_helper(self, vertex, visited):
        # Mark the current vertex as visited
        visited[vertex] = True
        print(vertex, end=" ")  # Print the visited vertex

        # Recur for all the vertices adjacent to this vertex
        for adjacent_vertex in self.adjacency_list[vertex]:
            if not visited[adjacent_vertex]:  # If not visited
                self._dfs_recursive_helper(adjacent_vertex, visited)

    def dfs_iterative(self, start_vertex):
        # Create a list to track visited vertices
        visited = [False] * self.num_vertices
        # Use a stack to keep track of vertices to visit
        stack = []

        # Push the starting vertex onto the stack
        stack.append(start_vertex)
        print("DFS traversal (iterative) starting from vertex", start_vertex, ":")

        while stack:
            # Pop a vertex from the stack
            vertex = stack.pop()
            if not visited[vertex]:  # If the vertex hasn't been visited
                visited[vertex] = True  # Mark it as visited
                print(vertex, end=" ")  # Print the visited vertex

                # Push all unvisited adjacent vertices onto the stack
                for adjacent_vertex in self.adjacency_list[vertex]:
                    if not visited[adjacent_vertex]:
                        stack.append(adjacent_vertex)

        print()  # Print a new line after DFS traversal


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

# Perform DFS starting from vertex 0
graph.dfs_recursive(0)  # Recursive DFS
graph.dfs_iterative(0)  # Iterative DFS
