from collections import deque

X = [-1, 1, 0, 0]
Y = [0, 0, -1, 1]

def BFS(M, N, pos, graph):
    bfs_queue = deque()
    bfs_queue.append(pos)
    graph[pos[0]][pos[1]] = 0

    while bfs_queue:
        x, y= bfs_queue.popleft()

        for i in range(4):
            if x + X[i] >= 0 and x + X[i] < N and y + Y[i] >= 0 and y + Y[i] < M:
                if graph[x + X[i]][y + Y[i]]:
                    bfs_queue.append((x + X[i], y + Y[i]))
                    graph[x + X[i]][y + Y[i]] = 0
    return

cases = int(input())

for i in range(cases):
    N, M, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]

    for j in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                count +=1
                BFS(M, N, (i,j), graph)
    
    print(count)
