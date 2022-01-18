dX = [0, 0, -1, 1]
dY = [-1, 1, 0, 0]
direction = ['U', 'D', 'L', 'R']
pos = [0,0]

def moveByDir(N, dir):
    global pos
    
    dr = direction.index(dir)

    pos[0] += dY[dr]
    pos[1] += dX[dr]

    if pos[0] < 0:
        pos[0] = 0
    elif pos[0] >= N:
        pos[0] = N-1

    if pos[1] < 0:
        pos[1] = 0
    elif pos[1] >= N:
        pos[1] = N-1

    return
        

def solution(N, directions):
    answer = [0, 0]
    dir_list = list(directions.split())

    for i in dir_list:
        moveByDir(N, i)

    answer[0] = pos[0]+1
    answer[1] = pos[1]+1

    return answer


print(solution(5, "R R R U D D"))