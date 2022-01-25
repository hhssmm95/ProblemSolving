dX = [0, 0, 1, -1]
dY = [1, -1, 0, 0]

def dfs(frame, index, visited):
    pos = index
    N = len(frame)
    M = len(frame[0])

    for i in range(4):
        x = pos[1] + dX[i]
        y = pos[0] + dY[i]

        if(x >= M or x < 0) or (y >= N or y < 0):
            continue

        if frame[y][x] == 0 and not visited[y][x]:
            visited[y][x] = True
            dfs(frame, (y, x), visited)
 

def solution(N, M, frame):
    answer = 0
    visited = [[False]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if frame[i][j] == 0 and not visited[i][j]:
                answer+=1
                visited[i][j] = True
                dfs(frame, (i, j), visited)

    return answer


print(solution(4, 6, [[0,1,0,1,0,1], [1,0,1,0,1,0], [0,1,0,1,0,1], [1,0,1,0,1,0]]))