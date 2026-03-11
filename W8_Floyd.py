# Floyd Warshall Algorithm - All Pairs Shortest Path

X = 999

# number of vertices
n = 4

# adjacency matrix
D = [
    [0,3,X,5],
    [2,0,X,4],
    [X,6,0,X],
    [X,X,2,0]
]

# Floyd Warshall Algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            if D[i][j] > D[i][k] + D[k][j]:
                D[i][j] = D[i][k] + D[k][j]

# print shortest distance matrix
print("Shortest Distance Matrix:")
for i in range(n):
    for j in range(n):
        print(D[i][j], end=" ")
    print()