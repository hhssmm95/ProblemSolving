from collections import deque

X = [-1, 1, 0, 0]
Y = [0, 0, -1, 1]


def bfs(N, pos, graph, bfs_visited):
    bfs_queue = deque()
    #bfs_visited = [[False] * N for _ in range(N)]

    bfs_queue.append(pos)
    bfs_visited[pos[0]][pos[1]] = True

    count = 0

    while bfs_queue:
        now = bfs_queue.popleft()
        count += 1

        for i in range(4):
            if now[0] + X[i] >= 0 and now[0] + X[i] < N and now[1] + Y[i] >= 0 and now[1] + Y[i] < N:
                if graph[now[0] + X[i]][now[1] + Y[i]] and not bfs_visited[now[0] + X[i]][now[1] + Y[i]]:
                    bfs_queue.append((now[0] + X[i], now[1] + Y[i]))
                    bfs_visited[now[0] + X[i]][now[1] + Y[i]] = True
    return count

def solution(N, graph):
    bfs_visited = [[False] * N for _ in range(N)]

    complex = 0
    house = []

    for i in range(N):
        for j in range(N):
            if graph[i][j] and not bfs_visited[i][j]:
                complex+=1
                house.append(bfs(N, (i,j), graph, bfs_visited))

    house.sort()
    print(complex)
    for i in house:
        print(i)


N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
solution(N, graph)



