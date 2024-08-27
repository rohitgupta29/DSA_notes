"""
Given an undirected and disconnected graph G(V, E), containing 'V' vertices and 'E' edges, the information about edges is given using 'GRAPH' matrix, where i-th edge is between GRAPH[i][0] and GRAPH[i][1]. print its DFS traversal.

V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.

E is the number of edges present in graph G.
Note :
The Graph may not be connected i.e there may exist multiple components in a graph.

Note: Make it work on the website too.
"""


def depth_first_search(v,e,edges):
  # Create an adjacency list to represent the graph 
  adj_list = [[] for _ in range(v)] 

  for edge in edges:
    source = edge[0]
    destination = edge[1]
    adj_list[source].append(destination)
    adj_list[destination].append(source)

  # List to keep track of visited vertices
  visited = [False] * v 

  # List to store all components found in the graph
  components = []

  # Perform DFS for each vertex 
  for i in range(v):
    if not visited[i]:
      component = []
      dfs(i, adj_list, visited, component) # Call dfs 
      component.append(sorted(component)) # sort the component and add to components list 

  return component 


def dfs(node, adj_list, visited, component):
  # Mark the current node as visited 
  visited[node] = True 
  component.append(node)  # Add the node to the current component 

  # Traverse the neighbours of the current node 
  for neighbour in adj_list[node]: 
    if not visited[neighbour]:
      dfs(neighbour, adj_list, visited, component)  # Recursively call dfs for the neighbour 




if __name__ == "__main__":

  v = 5 # no. of vertices 
  e = 4 # no. of edges

  edges = [
      [0,2],
      [0,1],
      [1,2],
      [3,4]
  ]

# call the function to perform dfs 
components = depth_first_search(v,e,edges)

print(len(components))

for component in components:
  print(" ".join(map(str, component)))
