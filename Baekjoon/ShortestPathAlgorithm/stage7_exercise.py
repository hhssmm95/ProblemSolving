import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
V,E = map(int, input().split())

graph = [[INF] * (V+1) for _ in range(V+1)]

for i in range(E):
    sv, dv, dist = map(int, input().split())
    graph[sv][dv] = dist

def floyd_warshall():
    for mid in range(1, V+1):
        for start in range(1, V+1):
            for dest in range(1, V+1):
                graph[start][dest] = min(graph[start][dest], graph[start][mid] + graph[mid][dest])

floyd_warshall()

min_cycle = INF
for i in range(1,V+1):
    min_cycle = min(min_cycle, graph[i][i])

if min_cycle == INF:
    print(-1)
else:   
    print(min_cycle)
