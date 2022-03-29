from collections import deque


X = [1, -1, 0, 0]
Y = [0, 0, 1, -1]


def BFS(N, M, start, graph):
    bfs_queue = deque()
    bfs_queue.append(((0,0),1))

    x = start[0]
    y = start[1]

    graph[x][y] = 0

    while bfs_queue:
        now = bfs_queue.popleft()
        x,y = now[0]
        count = now[1]
        for i in range(4):
            if x + X[i] >= 0 and x + X[i] < N and y + Y[i] >= 0 and y + Y[i] < M:
                if graph[x + X[i]][y + Y[i]]:
                    if x + X[i] == N-1 and y + Y[i] == M-1:
                        return count +1
                    else:
                        bfs_queue.append(((x + X[i], y + Y[i]), count+1))
                        graph[x + X[i]][y + Y[i]] = 0


N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
print(BFS(N, M, (0,0), graph))