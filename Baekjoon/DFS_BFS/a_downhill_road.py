from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
heightMap = []
for i in range(M):
    heightMap.append(list(map(int,input().split())))

R = [1,-1,0,0]
C = [0,0,1,-1]
DIR = 4

cache = [[-1]*N for _ in range(M)]

def DFS(pos):
    r, c = pos
    if pos == (M-1, N-1):
        return 1
    if cache[r][c] != -1:
        return cache[r][c]

    cache[r][c] = 0
    
    for i in range(DIR):
        nr = r + R[i]
        nc = c + C[i]

        if 0 <= nr < M and 0 <= nc < N:
            if heightMap[nr][nc] < heightMap[r][c]:
                cache[r][c] += DFS((nr,nc))

    return cache[r][c]

def BFS():
    bfs_queue = deque()
    bfs_queue.append((0,0))
    count = 0
    while bfs_queue:
        r,c = bfs_queue.popleft()

        if (r,c) == (M-2,N-1) or (r,c) == (M-1,N-2):
            count+=1
            continue

        for i in range(DIR):
            nr = r + R[i]
            nc = c + C[i]

            if 0 <= nr < M and 0 <= nc < N:
                if heightMap[nr][nc] < heightMap[r][c]:
                    bfs_queue.append((nr,nc))
    print(count)

print(DFS((0,0)))
