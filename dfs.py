# Depth First Search using Recursion

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)


# Input Section
graph = {}

vertices = int(input("Enter number of vertices: "))

for i in range(vertices):
    vertex = input(f"Enter vertex {i + 1}: ")
    neighbours = input(f"Enter neighbours of {vertex} separated by space: ").split()
    graph[vertex] = neighbours

start = input("Enter starting vertex: ")

visited = set()

print("\nDFS Traversal:")
dfs(graph, start, visited)
