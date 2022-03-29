from collections import deque


HEIGHT = [1, -1, 0, 0, 0, 0]
ROW = [0, 0, 1, -1, 0, 0]
COLUMN = [0, 0, 0, 0, 1, -1]

def BFS(H, M, N, graph, bfs_queue):

    while bfs_queue:
        h, r, c = bfs_queue.popleft()
        
        for i in range(6):
            nh = h + HEIGHT[i]
            nr = r + ROW[i]
            nc = c + COLUMN[i]

            if nh >= 0 and nh < H and nr >= 0 and nr < N and nc >= 0 and nc < M and graph[nh][nr][nc] == 0:
                    bfs_queue.append((nh, nr, nc))
                    graph[nh][nr][nc] = graph[h][r][c] + 1



M, N, H = map(int, input().split())
graph = [[] * N for _ in range(H)]
for i in range(H):
    for j in range(N):
        graph[i].append(list(map(int, input().split())))

bfs_queue = deque()

flag = False
for h in range(H):
    for r in range(N):
        for c in range(M):
            if graph[h][r][c] == 1:
                bfs_queue.append((h,r,c))
            if not flag and graph[h][r][c] == 0:
                flag = True

if not flag:
    print(0)
    exit(0)

BFS(H, M, N, graph, bfs_queue)

end_day = -1
for h in range(H):
    for r in range(N):
        end_day = max(end_day, max(graph[h][r]))
        if 0 in graph[h][r]:
            print(-1)
            exit(0)

print(end_day-1)


