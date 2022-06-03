from copy import deepcopy

def getScore(apeach, lion):
    apeachScore = 0
    lionScore = 0
    for i in range(11):
        if apeach[i] >= lion[i]:
            if apeach[i] == 0:
                continue
            apeachScore += 10-i
        else:
            lionScore += 10-i

    return lionScore - apeachScore

biggest = -1
biggestInfo = []

def DFS(lion,apeach,arrow,idx):
    if arrow==0 or idx >= len(lion):
        global biggest, biggestInfo
        result = getScore(apeach, lion)
        if result <= 0:
            return

        if result > biggest:
            biggest = result
            biggestInfo = deepcopy(lion)
        elif result == biggest:
            for i in range(1, 11):
                if lion[-i] > biggestInfo[-i]:
                    biggestInfo = deepcopy(lion)
                    break
                elif lion[-i] < biggestInfo[-i]:
                    break

    elif idx == len(lion)-1:
        lion[idx]=arrow
        DFS(lion, apeach, 0, idx+1)
        lion[idx]=0
    else:
        if arrow > apeach[idx]:
            lion[idx]=apeach[idx]+1
            DFS(lion, apeach, arrow-(apeach[idx]+1), idx+1)
            lion[idx]=0
        DFS(lion, apeach, arrow, idx+1)
        
    return
        


def solution(n, info):
    DFS([0]*11,info,n,0)

    return biggestInfo if biggest > -1 else [-1]

print(solution(9,	[0,0,1,2,0,1,1,1,1,1,1]))