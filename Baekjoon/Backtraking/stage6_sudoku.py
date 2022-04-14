import sys
input = sys.stdin.readline

sudoku = []
blank = []
for i in range(9):
    sudoku.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i,j))


def backtraking(idx):

    if idx >= len(blank):
        return True

    pos = blank[idx]

    for i in range(1,10):
        #행 검사
        if i in sudoku[pos[0]]:
            continue
        isExist = False
        #열 검사
        for j in range(9):
            if sudoku[j][pos[1]] == i:
                isExist = True
                break
        if isExist:
            continue
        # 3x3 블록 검사
        for j in range(3):
            if isExist:
                break

            row = pos[0]//3 * 3 + j

            for k in range(3):
                col = pos[1]//3 * 3 + k

                if sudoku[row][col] == i:
                    isExist = True
                    break
        if isExist:
            continue

        #중복이 아니라면
        sudoku[pos[0]][pos[1]] = i

        if not backtraking(idx+1):
            sudoku[pos[0]][pos[1]] = 0
        else:
            return True
    return False

backtraking(0)
#print('------------------')
for i in range(9):
    for j in range(9):
        print(sudoku[i][j], end = ' ')
    print()
