import sys

sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
count = 1


def dfs(graph, v, visited):
    global count
    visited[v] = count

    for i in graph[v]:
        if visited[i] == 0:
            count += 1
            dfs(graph, i, visited)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for j in range(n + 1):
    graph[j].sort(reverse=True)

dfs(graph, r, visited)

for i in range(1, n + 1):
    if visited[i] != 0:
        print(visited[i])
    else:
        print(0)
