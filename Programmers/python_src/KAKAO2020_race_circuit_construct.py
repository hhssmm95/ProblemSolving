from collections import deque

R = [1,-1,0,0]
C = [0,0,1,-1]
DIR = 4
INF=int(1e9)
def BFS(N, board):
    visited = [[[INF] * N for _ in range(N)] for _ in range(4)]
    
    bfsQ = deque()
    bfsQ.append((0,0,-1,0))

    while bfsQ:
        r,c,dir,cost = bfsQ.popleft()

        for i in range(DIR):
            nr = r + R[i]
            nc = c + C[i]

            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] == 1:
                    continue
               
                ncost = cost + (100 if dir == i or dir == -1 else 600)
                if visited[i][nr][nc] < ncost:
                    continue

                visited[i][nr][nc] = ncost
                if (nr,nc) != (N-1,N-1):
                    bfsQ.append((nr,nc,i,ncost))

    min_cost = INF
    for i in range(DIR):
        min_cost = min(min_cost,visited[i][N-1][N-1])
    return min_cost


   
def solution(board):
    N = len(board)
    return BFS(N, board)


print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))


'''cases
입출력 예
board	result
[[0,0,0],[0,0,0],[0,0,0]]	900
[[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]	3800
[[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]	2100
[[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]	3200
'''