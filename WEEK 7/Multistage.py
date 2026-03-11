import math

def multi_stage_graph(graph, stages, source, destination):
    n = len(graph)
    
    # Initialize cost array
    cost = [math.inf] * n
    path = [0] * n
    
    cost[destination] = 0   # Cost of destination = 0
    
    # Compute cost from last stage to first
    for i in range(n - 1, -1, -1):
        for (v, w) in graph[i]:
            if cost[v] + w < cost[i]:
                cost[i] = cost[v] + w
                path[i] = v
    
    # Reconstruct path
    min_path = []
    current = source
    while current != destination:
        min_path.append(current)
        current = path[current]
    min_path.append(destination)
    
    return cost[source], min_path

graph = {
    0: [(1, 2), (2, 2), (3, 3)],
    1: [(4, 4), (5, 11)],
    2: [(4, 9), (5, 5), (6, 16)],
    3: [(6, 2)],
    4: [(7, 18)],
    5: [(7, 13)],
    6: [(7, 2)],
    7: []
}

stages = 4
source = 0
destination = 7

min_cost, min_path = multi_stage_graph(graph, stages, source, destination)

print("Minimum Cost:", min_cost)
print("Minimum Path:", [node for node in min_path])
