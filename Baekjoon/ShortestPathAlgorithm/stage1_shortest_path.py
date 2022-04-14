import heapq
import sys
input = sys.stdin.readline

V, E =  map(int, input().split())
start_vertex = int(input())
graph = [[] for _ in range(V+1)]
distances = [1e9] * (V+1)

for i in range(E):
    edge = list(map(int, input().split()))
    graph[edge[0]].append((edge[1], edge[2]))

def dijkstra(start):
    h = []
    distances[start] = 0
    heapq.heappush(h, (distances[start], start))

    while h:
        curr_dist, curr_dest = heapq.heappop(h)

        if distances[curr_dest] < curr_dist:
            continue

        for data in graph[curr_dest]:
            new_dist = curr_dist + data[1]

            if distances[data[0]] > new_dist:
                distances[data[0]] = new_dist
                heapq.heappush(h, (new_dist, data[0]))

dijkstra(start_vertex)
for i in range(1, V+1):
    if i == start_vertex:
        print(0)
    else:
        if distances[i] == 1e9:
            print('INF')
        else:
            print(distances[i])
