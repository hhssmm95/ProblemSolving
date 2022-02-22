def solution(n, m, gold):
    cache = [[0]* m for _ in range(n)]

    for col in range(m):
        for row in range(n):
            if col == 0:
                cache[row][col] = gold[row][col]
            else:
                top = 0
                mid = cache[row][col-1]
                bottom = 0

                if row > 0:
                    top = cache[row-1][col-1]
                if row < n-1:
                    bottom = cache[row+1][col-1]

                cache[row][col] = gold[row][col] + max(top, max(mid, bottom))

    answer = 0
    for i in range(n):
        if cache[i][m-1] > answer:
            answer = cache[i][m-1]
    return answer


    #dp[i][j] = array[i][j] + max(gold[i-1][j-1], gold[i][j-1], gold[i+1][j-1])

#print(solution(3,4, [[1,3,3,2], [2,1,4,1], [0,6,4,7]]))
print(solution(4,4, [[1,3,1,5], [2,2,4,1], [5,0,2,3], [0,6,1,2]]))