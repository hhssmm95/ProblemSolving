from collections import deque
import sys
input = sys.stdin.readline

def BFS(V, E, graph, visited, start, color):
    bfs_queue = deque([start])
    visited[start] = color

    while bfs_queue:
        curr = bfs_queue.popleft()

        for i in graph[curr]:
            if not visited[i]:
                bfs_queue.append(i)
                visited[i] = -visited[curr]
            elif visited[i] == visited[curr]:
                return False
    return True


cases = int(input())

for i in range(cases):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    for i in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    result = True

    for i in range(1, V+1):
        if not visited[i]:
            if not BFS(V,E,graph,visited,i,1):
                result = False
                break
    if result:
        print('YES')
    else:
        print('NO')

    

