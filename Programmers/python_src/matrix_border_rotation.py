R = [1,0,-1,0]
C = [0,1,0,-1]

R = [1,0,-1,0]
C = [0,1,0,-1]



def rotate(board, query):
    r1,c1,r2,c2 = query
    min_num = 10002
    border_count = (r2-r1 + c2-c1) *2

    r = r1-1
    c = c1-1
    dir = 0
    for i in range(border_count-1):
        if i == abs(r2-r1):
            dir+=1
        elif i == abs(r2-r1)+abs(c2-c1):
            dir+=1
        elif i == 2*abs(r2-r1)+abs(c2-c1):
            dir+=1
        
        nr = r+R[dir]
        nc = c+C[dir]

        min_num = min(min_num, board[nr][nc])
        board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
        r,c = nr, nc
    min_num = min(min_num, board[r][c])

        
    
    return min_num


def solution(rows, columns, queries):
    answer = []
    board = [[i*columns + j+1 for j in range(columns)] for i in range(rows)]
    for query in queries:
            answer.append(rotate(board,query))

    
    return answer
    
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))