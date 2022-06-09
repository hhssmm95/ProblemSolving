from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
heightMap = []
maxHeight = 0
for i in range(N):
    data = list(map(int,input().split()))
    maxHeight = max(maxHeight, max(data))

    heightMap.append(data)

R = [1,-1,0,0]
C = [0,0,1,-1]
DIR = 4

def BFS(pos,h,visited):
    bfs_queue = deque()
    bfs_queue.append(pos)

    while bfs_queue:
        r,c = bfs_queue.popleft()

        for i in range(DIR):
            nr = r + R[i]
            nc = c + C[i]

            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and heightMap[nr][nc] > h:
                    visited[nr][nc] = True
                    bfs_queue.append((nr,nc))

  

def solution():
    max_zone = 1
    for h in range(1,maxHeight+1):
        visited = [[False]*N for _ in range(N)]
        zone = 0
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and heightMap[i][j] > h:
                    zone+=1
                    visited[i][j] = True
                    BFS((i,j),h,visited)
        max_zone = max(max_zone, zone)

    print(max_zone)

solution()
