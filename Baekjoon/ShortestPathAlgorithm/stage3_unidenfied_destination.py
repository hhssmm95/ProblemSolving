import heapq
import sys
input = sys.stdin.readline

cases = int(input())

for i in range(cases):
    #vertex, edge, number of destination
    v, e, nd = map(int,input().split())
    #start vertex, include_vertex1, include_vertex2
    s, v1, v2 = map(int, input().split())
    graph = [[] for _ in range(v+1)]

    for i in range(e):
        edge = list(map(int, input().split()))
        graph[edge[0]].append((edge[1], edge[2]))
        graph[edge[1]].append((edge[0], edge[2]))

    #candidate destinations
    dests = []

    for i in range(nd):
        dests.append(int(input()))

    def dijkstra(start):
        distances = [1e9]*(v+1)
        h = []
        
        distances[start] = 0
        heapq.heappush(h, (distances[start], start))

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

    first_dists = dijkstra(s)
    v1_dists = dijkstra(v1)
    v2_dists = dijkstra(v2)

    dests.sort()
    for i in dests:
        total1 = first_dists[v1] + v1_dists[v2] + v2_dists[i]
        total2 = first_dists[v2] + v2_dists[v1] + v1_dists[i]

        # s->v1->v2->i  혹은  s->v2->v1->i가 s부터 i까지의 최단거리라면 출력
        if total1 == first_dists[i] or total2 == first_dists[i]:
            print(i, end =' ')
    print()