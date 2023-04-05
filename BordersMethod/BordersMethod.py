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
    next_node = -1
    current_node = path[-1]
        
    for j in range(n):
        if not visited[j] and graph[current_node][j] < min_dist:
            min_dist = graph[current_node][j]
            dist += min_dist
            next_node = j  
    visited[next_node] = True
    path.append(next_node)
        
path.append(0)
print(path, dist)
#[0, 4, 1, 2, 3, 0] 85

