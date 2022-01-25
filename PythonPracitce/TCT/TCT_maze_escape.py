from collections import deque

dX = [1,-1,0,0]
dY = [0,0,1,-1]

def bfs(map, visited):
    pos = (0,0)
    N = len(map)
    M = len(map[0])

    q = deque()
    q.append((pos, 0))
    visited[pos[0]][pos[1]] = True

    while q:
        qtup = q.popleft()
        cpos = qtup[0]
        mcount = qtup[1]

        for i in range(4):
            x = cpos[0] + dX[i]
            y = cpos[1] + dY[i]
            if x < 0 or x >= N or y < 0 or y >= M:
                continue
            elif x == N-1 and y == M-1:
                return mcount+2

            if map[x][y] == 1 and not visited[x][y]:
                visited[x][y] = True
                q.append(((x,y), mcount+1))



def solution(N, M, map):
    answer = 0
    visited = [[False]*M for _ in range(N)]
    answer = bfs(map, visited)

    return answer


print(solution(5, 6, [[1,1,1,1,1,1], [1,0,0,0,0,1], [0,0,0,1,1,1],[0,0,0,1,0,0],[1,1,1,1,1,1]]))


