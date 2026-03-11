# Bellman-Ford Algorithm - Single Source Shortest Path

# number of vertices
V = 5

# edges: (u, v, weight)
E = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (4, 3, -3)
]

# source vertex
S = 0

# distance initialization
dist = [999] * V
parent = [None] * V

dist[S] = 0

# relax edges |V|-1 times
for i in range(V - 1):
    for u, v, w in E:
        if dist[u] != 999 and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            parent[v] = u

# check for negative weight cycle
for u, v, w in E:
    if dist[u] != 999 and dist[u] + w < dist[v]:
        print("Negative weight cycle exists")
        break

# print distances
print("Vertex Distance from Source")
for i in range(V):
    print(i, "\t", dist[i])

# print shortest paths
print("\nShortest Paths:")
for i in range(V):
    path = []
    current = i
    
    while current is not None:
        path.append(current)
        current = parent[current]
        
    path.reverse()
    
    print("Path to", i, ":", path)
