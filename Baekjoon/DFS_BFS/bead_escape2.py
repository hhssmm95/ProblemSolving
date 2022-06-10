from copy import deepcopy
import sys
input = sys.stdin.readline

N, M  = map(int, input().split())
board = []
srPos = (-1,-1)
sbPos = (-1,-1)
goalPos = (-1,-1)

for i in range(N):
    line = list(input().strip())

    for j, val in enumerate(line):
        if srPos != (-1,-1) and sbPos != (-1,-1) and goalPos != (-1,-1):
            break
        else:
            if val == 'R':
                srPos = (i,j)
            elif val == 'B':
                sbPos = (i,j)
            elif val == 'O':
                goalPos = (i,j)


    board.append(line)

R = [1,-1,0,0]
C = [0,0,1,-1]
DIR = 4
INF=int(1e9)

def tiltBead(Pos, dir, board):
    r, c = Pos

    nr = r + R[dir]
    nc = c + C[dir]

    while board[nr][nc] != '#':

        if board[nr][nc] == 'O':
            return (nr,nc)
        else:
            nr += R[dir]
            nc += C[dir]
            
    return (nr-R[dir],nc-C[dir])


def tilt(rPos, bPos, dir, board):
    nrPos = tiltBead(rPos, dir, board)
    nbPos = tiltBead(bPos, dir, board)

    RMoveDistance = abs(nrPos[0] - rPos[0]) + abs(nrPos[1] - rPos[1])
    BMoveDistance = abs(nbPos[0] - bPos[0]) + abs(nbPos[1] - bPos[1])

    if board[nbPos[0]][nbPos[1]] == 'O':
        return (-1, nrPos, nbPos,board)
    if board[nrPos[0]][nrPos[1]] == 'O':
        return (1, nrPos, nbPos,board)
    
    if nrPos == nbPos:
        if RMoveDistance > BMoveDistance:
            nrPos = (nrPos[0] - R[dir], nrPos[1] - C[dir])
        else:
            nbPos = (nbPos[0] - R[dir], nbPos[1] - C[dir])

    board[rPos[0]][rPos[1]], board[nrPos[0]][nrPos[1]] = board[nrPos[0]][nrPos[1]] ,board[rPos[0]][rPos[1]]
    board[bPos[0]][bPos[1]], board[nbPos[0]][nbPos[1]] = board[nbPos[0]][nbPos[1]] ,board[bPos[0]][bPos[1]]

    return (0, nrPos, nbPos, board)

answer = int(1e9)
visited = [[[[INF] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

def DFS(rPos, bPos, N, board):
    global answer
    rr, rc = rPos
    br, bc = bPos
    print(rPos)

    for dir in range(DIR):
        result = tilt(rPos, bPos, dir, deepcopy(board))
        nrPos = result[1]
        nbPos = result[2]
        nboard = result[3]
        nrr,nrc = nrPos
        nbr,nbc = nbPos

        if result[0] == -1:
            continue
        elif result[0] == 1:
            visited[nrr][nrc][nbr][nbc] = min(visited[nrr][nrc][nbr][nbc], visited[rr][rc][br][bc] + 1)
        else:
            if visited[rr][rc][br][bc] +1 < visited[nrr][nrc][nbr][nbc]:
                visited[nrr][nrc][nbr][nbc] = visited[rr][rc][br][bc] +1
                DFS(nrPos, nbPos, N, nboard)


visited[srPos[0]][srPos[1]][sbPos[0]][sbPos[1]] = 0
DFS(srPos, sbPos, N, board)
answer = int(1e9)
for i in range(N):
    for j in range(M):
        answer = min(answer,visited[goalPos[0]][goalPos[1]][i][j])
print(answer if answer <= 10 else -1)
            

            


