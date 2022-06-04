from copy import deepcopy
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
MAP = []
virus = []
except_wall_size = N*M-3
for i in range(N):
    data = list(map(int,input().split()))
    for j, val in enumerate(data):
        if val == 2:
            virus.append((i,j))
        elif val == 1:
            except_wall_size-=1
    MAP.append(data)

R = [1,-1,0,0]
C = [0,0,1,-1]
answer = 0

def DFS():
    global answer
    total = 0
    tmp_MAP = deepcopy(MAP)
    for vR, vC in virus:
        #visited = [[False]*M for _ in range(N)]
        vStack = [(vR,vC)]
        vSize = 0

        while vStack:
            r,c = vStack.pop()
            vSize+=1

            for dir in range(4):
                nr = r + R[dir]
                nc = c + C[dir]

                if 0<=nr<N and 0<=nc<M:
                    if tmp_MAP[nr][nc] != 0:
                        continue
                    tmp_MAP[nr][nc] = 2
                    vStack.append((nr,nc))
        total += vSize
    
    answer = max(answer, except_wall_size - total)

def makeWall(count):
    if count == 3:
        DFS()
        return
    
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 0:
                MAP[i][j] = 1
                makeWall(count+1)
                MAP[i][j] = 0


makeWall(0)
print(answer)
    

