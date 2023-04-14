import sys
graph = [
    [0, 14, 55, 7, 5],
    [8, 0, 5, 46, 36],
    [31, 15, 0, 29, 6],
    [37, 5, 6, 0, 22],
    [6, 25, 31, 38, 0]
]
n = len(graph)
visited = [False] * n
path = [0]
visited[0] = True
dist = 0
for i in range(n-1):
    min_dist = sys.maxsize
    next = -1
    current = path[-1]
        
    for j in range(n):
        if not visited[j] and graph[current][j] < min_dist:
            min_dist = graph[current][j]
            dist += min_dist
            next = j  
    visited[next] = True
    path.append(next)
        
path.append(0)
print(path, dist)
#[0, 4, 1, 2, 3, 0] 85

