import heapq
import sys
input = sys.stdin.readline

V, E =  map(int, input().split())
graph = [[] for _ in range(V+1)]

for i in range(E):
    edge = list(map(int, input().split()))
    graph[edge[0]].append((edge[1], edge[2]))
    graph[edge[1]].append((edge[0], edge[2]))

v1, v2 = map(int, input().split())
if v1>v2:
    temp = v1
    v1 = v2
    v2 = temp

def dijkstra(start):
    distances = [1e9] * (V+1)
    h = []
    distances[start] = 0
    heapq.heappush(h, (distances[start], start))
    shortest = 1e9

    while h:
        curr_dist, curr_vertex = heapq.heappop(h)

        if distances[curr_vertex] < curr_dist:
            continue


        for data in graph[curr_vertex]:
            new_dist = curr_dist + data[1]
           
            if distances[data[0]] > new_dist:
                distances[data[0]] = new_dist
                heapq.heappush(h, (new_dist, data[0]))
    return distances

first_dists = dijkstra(1)
v1_dists = dijkstra(v1)
v2_dists = dijkstra(v2)
total = min(first_dists[v1] + v1_dists[v2] + v2_dists[V], first_dists[v2] + v2_dists[v1] + v1_dists[V])

if total >= 1e9:
    print(-1)
else:
    print(total)
