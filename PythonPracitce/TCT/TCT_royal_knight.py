dX = [1, 1, -1, -1, 2, 2,-2,-2]
dY = [2, -2, 2, -2, 1, -1, 1, -1]


def solution(pos):
    answer = 0
    posX = ord(pos[0]) - ord('a') + 1
    posY = int(pos[1])

    for i in range(8):
        X = posX + dX[i] - 1
        Y = posY + dY[i] - 1

        if X >= 0 and X < 8 and Y >= 0 and Y < 8:
            answer+=1

    return answer

print(solution('a1'))