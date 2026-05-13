# A* Algorithm

def a_star(graph, heuristics, start, goal):
    open_list = [start]
    closed_list = []

    g = {}
    g[start] = 0

    parents = {}
    parents[start] = start

    while len(open_list) > 0:
        n = None

        # Find node with lowest f = g + h
        for v in open_list:
            if n is None or g[v] + heuristics[v] < g[n] + heuristics[n]:
                n = v

        if n == goal:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start)
            path.reverse()

            print("Path found:", path)
            return

        for (m, weight) in graph[n]:
            if m not in open_list and m not in closed_list:
                open_list.append(m)
                parents[m] = n
                g[m] = g[n] + weight

            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.append(m)

        open_list.remove(n)
        closed_list.append(n)

    print("Path does not exist!")


# Input Section
graph = {}
heuristics = {}

nodes = int(input("Enter number of nodes: "))

for i in range(nodes):
    node = input(f"Enter node {i+1}: ")

    h = int(input(f"Enter heuristic value for {node}: "))
    heuristics[node] = h

    neighbour_count = int(input(f"Enter number of neighbours for {node}: "))

    neighbours = []

    for j in range(neighbour_count):
        neighbour = input("Enter neighbour node: ")
        weight = int(input("Enter edge cost: "))
        neighbours.append((neighbour, weight))

    graph[node] = neighbours

start = input("Enter start node: ")
goal = input("Enter goal node: ")

a_star(graph, heuristics, start, goal)
