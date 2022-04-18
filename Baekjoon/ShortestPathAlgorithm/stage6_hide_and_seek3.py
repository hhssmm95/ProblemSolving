import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
INF = 1e9

start = min(N,K)
end = max(N,K)
graph = [[] for _ in range(100001)]
distances = [INF]*(100001)

for i in range(100001):
    if i*2 >= 0 and i*2 <= 100000:
        graph[i].append((i*2, 0))
    if i+1 >= 0 and i+1 <= 100000:
        graph[i].append((i+1, 1))
    if i-1 >= 0 and i-1 <= 100000:
        graph[i].append((i-1, 1))

def dijkstra(start_vertex):
    distances[start_vertex] = 0
    h = []
    heapq.heappush(h, (0, start_vertex))

    while h:
        time, curr_vertex = heapq.heappop(h)
        if distances[curr_vertex] < time:
            continue
        for next_vertex, add_time in graph[curr_vertex]:
            new_time = time + add_time

            if distances[next_vertex] > new_time:
                distances[next_vertex] = new_time
                heapq.heappush(h, (new_time, next_vertex))

dijkstra(N)
print(distances[K])
