from collections import deque


R = [-1,1,0,0]
C = [0,0,-1,1]

LL, LR, RL, RR = (4,5,6,7)
RR = 7

def checkRotation(pos1, pos2, isVertical, dir, board, N):
    p1, p2 = (pos1, pos2)
    result = True

    if not isVertical:
        if p2[1] < p1[1]:
            p1, p2 = p2, p1
        nr1, nc1 = p1
        nr2, nc2 = p2

            
        if dir == LL:
            nr2, nc2 = (p1[0]-1, p1[1])
            if (0 > p2[0]-1 or 0 > p1[0]-1 or board[p2[0]-1][p2[1]] == 1 or board[p1[0]-1][p1[1]] == 1):
                result = False
        elif dir == LR :
            nr2, nc2 = (p1[0]+1, p1[1])
            if (p2[0]+1 >= N or p1[0]+1 >= N or board[p2[0]+1][p2[1]] == 1 or board[p1[0]+1][p1[1]] == 1):
                result = False
        elif dir == RL:
            nr1, nc1 = (p2[0]+1, p2[1])
            if (p1[0]+1 >= N or p2[0]+1 >= N or board[p1[0]+1][p1[1]] == 1 or board[p2[0]+1][p2[1]] == 1):
                result = False
        elif dir == RR:
            nr1, nc1 = (p2[0]-1, p2[1])
            if (0 > p1[0]-1 or 0 > p2[0]-1 or board[p1[0]-1][p1[1]] == 1 or board[p2[0]-1][p2[1]] == 1):
                result = False

    else:
        if p2[0] < p1[0]:
            p1, p2 = p2, p1
        nr1, nc1 = p1
        nr2, nc2 = p2

        if dir == LL:
            nr2, nc2 = (p1[0], p1[1]+1)
            if (p2[1]+1 >= N or p1[1]+1 >= N or board[p2[0]][p2[1]+1] or board[p1[0]][p1[1]+1] == 1):
                result =  False
        elif dir == LR:
            nr2, nc2 = (p1[0], p1[1]-1)
            if (0 > p2[1]-1 or 0 > p1[1]-1 or board[p2[0]][p2[1]-1] or board[p1[0]][p1[1]-1] == 1):
                result =  False
        elif dir == RL:
            nr1, nc1 = (p2[0], p2[1]-1)
            if (0 > p1[1]-1 or 0 > p2[1]-1 or board[p1[0]][p1[1]-1] or board[p2[0]][p2[1]-1] == 1):
                result = False
        elif dir == RR:
            nr1, nc1 = (p2[0], p2[1]+1)
            if (p1[1]+1 >= N or p2[1]+1 >= N or board[p1[0]][p1[1]+1] or board[p2[0]][p2[1]+1] == 1):
                result = False
    
    return [result, nr1, nc1, nr2, nc2]


def BFS(board):
    N = len(board)
    time = 0

    visited = set()
    q = deque()

    visited.add(((0,0), (0,1)))
    visited.add(((0,1),(0,0)))

    q.append([(0,0),(0,1),0,False])

    while q:
        pos1, pos2, time, isVertical = q.popleft()
        r1,c1 = pos1
        r2,c2 = pos2

        if (r1,c1) == (N-1,N-1) or (r2,c2) == (N-1,N-1):
            return time

        for dir in range(8):
            if dir < 4:
                nr1, nc1 = (r1 + R[dir], c1 + C[dir])
                nr2, nc2 = (r2 + R[dir], c2 + C[dir])

                if 0<= nr1 < N and 0 <= nc1 < N and 0 <= nr2 < N and 0 <= nc2 < N:
                    if ((nr1,nc1),(nr2,nc2)) in visited or board[nr1][nc1] == 1 or board[nr2][nc2] == 1:
                        continue
                    visited.add(((nr1,nc1),(nr2,nc2)))
                    visited.add(((nr2,nc2),(nr1,nc1)))
                    q.append([(nr1,nc1),(nr2,nc2),time+1,isVertical])
            else:
                result, nr1, nc1, nr2, nc2 = checkRotation((r1,c1),(r2,c2),isVertical,dir,board,N)

                if result:
                    if ((nr1,nc1),(nr2,nc2)) not in visited:
                        visited.add(((nr1,nc1),(nr2,nc2)))
                        visited.add(((nr2,nc2),(nr1,nc1)))
                        q.append([(nr1,nc1),(nr2,nc2),time+1,not isVertical])



def solution(board):
    answer = BFS(board)
    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))

'''
board	result
[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	7
'''