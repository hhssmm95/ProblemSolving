import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


def DFS(start):
    dfs_stack = [start]

    while dfs_stack:
        node = dfs_stack.pop()

        for neighbor in graph[node]:
            if visited[neighbor]:
                continue
            visited[neighbor] = True
            dfs_stack.append(neighbor)

    return


visited = [False]*(N+1)
answer = 0

for i in range(1,N+1):
    if visited[i]:
        continue
    answer+=1
    visited[i] == True
    DFS(i)

print(answer)