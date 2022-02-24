from re import L


INF = 1e9

def solution(n, m, graph_info):
    graph = [[INF] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in graph_info[i]:
            if graph[i][i] == INF:
                graph[i][i] = 0

            graph[i][j[0]] = j[1]

    floyd_warshall(n, graph)

    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == INF:
                print(f"node {i} 에서 node {j} 까지의 최단거리: INFINITY")
            else:
                print(f"node {i} 에서 node {j} 까지의 최단거리: {graph[i][j]}")


def floyd_warshall(n, graph):

    for i in range (1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

solution(4, 7, [[], [(2,4), (4,6)], [(1,3), (3,7)], [(1,5), (4,4)], [(3,2)]])