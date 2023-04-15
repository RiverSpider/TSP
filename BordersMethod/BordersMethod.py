graph = [
    [0, 14, 55, 7, 5],
    [8, 0, 5, 46, 36],
    [31, 15, 0, 29, 6],
    [37, 5, 6, 0, 22],
    [6, 25, 31, 38, 0]
]
def getnodes(n):
    if n == 1:
        return [[0]]
    else:
        nodes = []
        for node in getnodes(n-1):
            for i in range(n):
                nnode = node[:i] + [n-1] + node[i:]
                nodes.append(nnode)
        return nodes

n = len(graph)
allnodes = getnodes(n)
mdistance = float('inf')
for node in allnodes:
    distance = 0
    for i in range(n-1):
        distance += graph[node[i]][node[i+1]]
    distance += graph[node[-1]][node[0]]
    if distance < mdistance:
        mdistance = distance
        route = node
print(route, mdistance)
#[4, 2, 3, 5, 1, 4] 29
