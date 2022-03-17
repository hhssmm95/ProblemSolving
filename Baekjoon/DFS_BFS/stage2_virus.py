result = 0

def recursive_dfs(node, graph, dfs_visited):
    dfs_visited[node] = True
    global result
    result += 1

    for i in graph[node]:
        if not dfs_visited[i]:
            recursive_dfs(i, graph, dfs_visited)


def solution(N, M, edges):
    graph = [[] for _ in range(N+1)]
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    dfs_visited = [False] * (N+1)

    recursive_dfs(1, graph, dfs_visited)
    print(result-1)

N = int(input())
M = int(input())
edges = []
for i in range(M):
    edges.append(tuple(map(int, input().split())))
solution(N, M, edges)


