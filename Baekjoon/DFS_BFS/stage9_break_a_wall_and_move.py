from collections import deque

R = [1, -1, 0, 0]
C = [0, 0, 1, -1]

def BFS(N, M, graph):
    bfs_queue = deque([(0,0,0)])

    visited = [[[0] * M for _ in range(N)] for _ in range(2)]
    visited[0][0][0] = 1

    while bfs_queue:
        r, c, broke = bfs_queue.popleft()
        if r == N-1 and c == M-1:
            return visited[broke][r][c]

        for i in range(4):
            nr = r + R[i]
            nc = c + C[i]

            if nr >= 0 and nr < N and nc >= 0 and nc < M:
                if graph[nr][nc] == 1 and broke == 0:
                    visited[1][nr][nc] = visited[0][r][c] +1
                    bfs_queue.append((nr, nc, 1))
                elif graph[nr][nc] == 0 and visited[broke][nr][nc] == 0:
                    visited[broke][nr][nc] = visited[broke][r][c] + 1
                    bfs_queue.append((nr,nc,broke))
    return -1
            
N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

print(BFS(N, M, graph))

