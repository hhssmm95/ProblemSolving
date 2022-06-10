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

print(DFS((0,0)))
