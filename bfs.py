# Breadth First Search

from collections import deque

def bfs(graph, start):

    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:

        vertex = queue.popleft()

        print(vertex, end=" ")

        for neighbour in graph[vertex]:

            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# Input Section
graph = {}

vertices = int(input("Enter number of vertices: "))

for i in range(vertices):
    vertex = input(f"Enter vertex {i + 1}: ")
    neighbours = input(f"Enter neighbours of {vertex} separated by space: ").split()
    graph[vertex] = neighbours

start = input("Enter starting vertex: ")

print("\nBFS Traversal:")
bfs(graph, start)
