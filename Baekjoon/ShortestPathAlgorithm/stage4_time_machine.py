import sys
input = sys.stdin.readline
INF = 1e9

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distances = [INF]*(N+1)

for i in range(M):
    edge = list(map(int, input().split()))
    graph[edge[0]].append((edge[1], edge[2]))

def bellman_ford():
    distances[1] = 0
    
    for i in range(N):
        for j in range(1, N+1):
            for dest, dist in graph[j]:
                new_dist = distances[j] + dist

                if distances[j] != INF and distances[dest] > new_dist:
                    #check cycle  
                    if i == N-1:
                        return 0

                    distances[dest] = new_dist
    return 1

if not bellman_ford():
    print(-1)
    exit(0)
else:
    for i in range(2, N+1):
        if distances[i] < 1e9:
            print(distances[i])
        else:
            print(-1)
