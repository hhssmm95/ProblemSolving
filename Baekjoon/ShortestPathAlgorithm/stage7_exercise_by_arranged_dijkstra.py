import heapq
import sys
input = sys.stdin.readline

INF = 1e9
V,E = map(int, input().split())


graph = [[] for _ in range(V+1)]
distances = [[INF] * (V+1) for _ in range(V+1)]

h = []

for i in range(E):
    sv, dv, dist = map(int, input().split())
    graph[sv].append((dv, dist))
    distances[sv][dv] = dist
    heapq.heappush(h, [dist, sv, dv])

while h:
    curr_dist, start, dest = heapq.heappop(h)

    if start == dest:
        print(curr_dist)
        break

    if distances[start][dest] < curr_dist:
        continue

    for next_dest, next_dist in graph[dest]:
        new_dist = curr_dist + next_dist

        if distances[start][next_dest] > new_dist:
            distances[start][next_dest] = new_dist
            heapq.heappush(h, [new_dist, start, next_dest])

else:
    print(-1)