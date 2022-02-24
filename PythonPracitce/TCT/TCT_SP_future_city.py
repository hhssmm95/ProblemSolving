INF = 1e9

def solution(N, M, graph_info, X, K):
    graph = [[INF] * (N+1) for _ in range(N+1)]

    for i in graph_info:
        graph[i[0]][i[1]] = 1
        graph[i[1]][i[0]] = 1

    for i in range(1, N+1):
        if graph[i][i] != 0:    
            graph[i][i] = 0

    print(f"{K}를 거쳐 {X}로 가는 최소 시간 : {floyd_warshal(N,X,K,graph)}")

def floyd_warshal(N, X, K, graph):

    min_val = INF
    for a in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i == 1 and a == K and j == X and graph[i][a] + graph[a][j] < min_val:
                    min_val = graph[i][a] + graph[a][j]

                graph[i][j] = min(graph[i][j], graph[i][a] + graph[a][j])

    return min_val


solution(5, 7, [(1,2), (1,3), (1,4), (2,4), (3,4), (3,5), (4,5)], 4, 5)
    
