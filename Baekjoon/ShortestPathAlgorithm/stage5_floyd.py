import sys
input = sys.stdin.readline
INF = 1e9

n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    sv, dv, cost = map(int, input().split())
    if graph[sv][dv] > cost:
        graph[sv][dv] = cost

def floyd_warshall():    
    for mid in range(1, n+1):
        for start in range(1, n+1):
            for dest in range(1, n+1):
                graph[start][dest] = min(graph[start][dest], graph[start][mid] + graph[mid][dest])


floyd_warshall()
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] < INF:
            print(graph[i][j], end=' ')
        else:
            print(0, end = ' ')
    print()