# Prim's Algorithm

INF = 9999999

n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")

G = []

for i in range(n):
    row = list(map(int, input().split()))
    G.append(row)

selected = [0] * n

selected[0] = True

edge_count = 0

print("\nEdges in Minimum Spanning Tree:")

while edge_count < n - 1:

    minimum = INF
    x = 0
    y = 0

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if (not selected[j]) and G[i][j]:
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j

    print(f"{x} - {y} : {G[x][y]}")

    selected[y] = True
    edge_count += 1
  
