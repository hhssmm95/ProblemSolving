from collections import deque


X = [1, -1, 0, 0]
Y = [0, 0, 1, -1]

def BFS(M, N, graph, bfs_queue):

    while bfs_queue:
        x,y = bfs_queue.popleft()
        
        for i in range(4):
            nx = x + X[i]
            ny = y + Y[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and graph[nx][ny] == 0:
                    bfs_queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1



M, N = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

bfs_queue = deque()

flag = False
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            bfs_queue.append((i,j))
        if not flag and graph[i][j] == 0:
            flag = True

if not flag:
    print(0)
    exit(0)

BFS(M, N, graph, bfs_queue)

end_day = -1
for i in range(N):
    end_day = max(end_day, max(graph[i]))
    if 0 in graph[i]:
        print(-1)
        exit(0)

print(end_day-1)


