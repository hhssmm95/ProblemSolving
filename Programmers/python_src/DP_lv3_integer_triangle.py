def solution(triangle):
    answer = 0
    n = len(triangle)

    for i in range(1, n):
        for j in range(i+1):
            left = -1 if j == 0 else triangle[i-1][j-1]
            right = -1 if j == i else triangle[i-1][j]

            triangle[i][j] = triangle[i][j] + max(left, right)
            if i == n-1:
                answer = max(answer, triangle[i][j])

    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
'''
[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	30
'''