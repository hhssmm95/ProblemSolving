def solution(n, results):
    answer = 0

    scoreBoard = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for A,B in results:
        scoreBoard[A][B] = 1
        scoreBoard[B][A] = -1

    for b in range(1,n+1):
        for a in range(1,n+1):
            for c in range(1,n+1):
                if scoreBoard[a][b] == 1 and scoreBoard[b][c] == 1:
                    scoreBoard[a][c] = 1
                    scoreBoard[c][a] = -1

    for scoreList in scoreBoard:
        if scoreList.count(0) == 2:
            answer+=1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

'''
n	results	return
5	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	2
'''