from copy import deepcopy
import sys
input = sys.stdin.readline

N = int(input())
cube = []
answer = 0
for i in range(N):
    line = list(map(int,input().split()))
    answer = max(answer,max(line))
    cube.append(line)

R = [1,-1,0,0]
C = [0,0,1,-1]
DIR = 4

def pushInDir(dir, temp_cube):
    global answer

    combined = [[False]*N for _ in range(N)]

    if dir < 2:
        i_start = N-2
        i_end = -1
        val = -1

        if dir == 1:
            i_start ,i_end =  (1, N)
            val = 1

        for i in range(i_start, i_end, val):
            for j in range(N):
                r = i
                nr = r+R[dir]

                if temp_cube[r][j] == 0:
                    continue

                while temp_cube[nr][j] == 0:
                    temp_cube[r][j], temp_cube[nr][j] = temp_cube[nr][j], temp_cube[r][j]
                    r = nr
                    nr +=R[dir]
                    if nr >= N  or nr < 0:
                        break
                
                if nr >= N  or nr < 0:
                    answer = max(answer, temp_cube[r][j])
                    continue


                if temp_cube[nr][j] == temp_cube[r][j] and not combined[nr][j]:
                    combined[nr][j] = True
                    temp_cube[nr][j] *=2
                    temp_cube[r][j] = 0
                    answer = max(answer, temp_cube[nr][j])

    else:
        j_start = N-2
        j_end = -1
        val = -1

        if dir == 3:
            j_start ,j_end =  (1, N)
            val = 1

        for j in range(j_start, j_end, val):
            for i in range(N):
                c = j
                nc = c+C[dir]
                
                if temp_cube[i][c] == 0:
                    continue

                while temp_cube[i][nc] == 0:
                    temp_cube[i][c], temp_cube[i][nc] = temp_cube[i][nc], temp_cube[i][c]
                    c = nc
                    nc +=C[dir]
                    if nc >= N  or nc < 0:
                        break

                if nc >= N  or nc < 0:
                    answer = max(answer, temp_cube[i][c])
                    continue

                if temp_cube[i][nc] == temp_cube[i][c] and not combined[i][nc]:
                    combined[i][nc] = True
                    temp_cube[i][nc] *=2
                    temp_cube[i][c] = 0
                    answer = max(answer, temp_cube[i][nc])
                
    return temp_cube


def DFS(new_cube, count):
    if count == 5:
        return
    
    for dir in range(DIR):
        DFS(pushInDir(dir, deepcopy(new_cube)), count+1)

DFS(cube,0)
print(answer)
