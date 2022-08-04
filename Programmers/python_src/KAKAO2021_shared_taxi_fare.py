def solution(n, s, a, b, fares):
    graph = [[int(1e9) if i != j else 0 for j in range(n+1)] for i in range(n+1)]
    for i,j,fee in fares:
        graph[i][j] = fee
        graph[j][i] = fee

    # floyd warshall
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    min_fee = int(1e9)

    for node in range(1,n+1):
        min_fee = min(min_fee, graph[s][node] + graph[node][a] + graph[node][b])

    return min_fee


print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))

'''
6	4	6	2	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]	82
7	3	4	1	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]	14
6	4	5	6	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
'''