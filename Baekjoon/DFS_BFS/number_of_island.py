from collections import deque
import sys
input = sys.stdin.readline

cases = []
while True:
    w,h = map(int, input().split())
    if (w,h) == (0,0):
        break

    isleMap = []
    
    for i in range(h):
        isleMap.append(list(map(int, input().split())))

    cases.append(((w,h),isleMap))

R = [1,-1,0,0,-1,-1,1,1]
C = [0,0,1,-1,-1,1,-1,1]
DIR = 8

def bfs(pos, w, h, Map, visited):
    bfs_queue = deque()
    bfs_queue.append(pos)

    while bfs_queue:
        r,c = bfs_queue.popleft()

        for dir in range(DIR):
            nr = r + R[dir]
            nc = c + C[dir]

            if 0 <= nr < h and 0 <= nc < w:
                if not visited[nr][nc] and Map[nr][nc] == 1:
                    visited[nr][nc] = True
                    bfs_queue.append((nr,nc))


def solution():
    for case in cases:
        w,h = case[0]
        isleMap = case[1]
        visited = [[False]*w for _ in range(h)]

        answer = 0

        for i in range(h):
            for j in range(w):
                if not visited[i][j] and isleMap[i][j]:
                    answer+=1
                    visited[i][j] = True
                    bfs((i,j), w, h, isleMap, visited)

        print(answer)

solution()
