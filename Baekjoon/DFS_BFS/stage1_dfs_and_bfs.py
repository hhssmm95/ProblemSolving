def recursive_dfs(node, graph, dfs_visited):
    dfs_visited[node] = True
    print(node, end=' ')

    for i in graph[node]:
        if not dfs_visited[i]:
            recursive_dfs(i, graph, dfs_visited)


def bfs(N, start, graph):
    bfs_queue = []
    bfs_visited = [False] * (N+1)

    bfs_queue.append(start)
    bfs_visited[start] = True

    while bfs_queue:
        now = bfs_queue.pop(0)
        print(now, end=' ')

        for i in graph[now]:
            if not bfs_visited[i]:
                bfs_queue.append(i)
                bfs_visited[i] = True

    print()

def solution(N, M, V, edges):
    graph = [[] for _ in range(N+1)]
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    for i in range(1, N+1):
        graph[i].sort()

    dfs_visited = [False] * (N+1)
    
    recursive_dfs(V, graph, dfs_visited)
    print()
    bfs(N, V, graph)

N, M, V = map(int, input().split())
edges = []
for i in range(M):
    edges.append(tuple(map(int, input().split())))
solution(N, M, V, edges)
