import heapq

INF = 1e9

def dijkstra(start, n, distance, graph):
    distance[start] = 0
    h = []
    heapq.heappush(h, (0, start))

    while h:
        dist,now = heapq.heappop(h)
        if distance[now] < dist:
            continue

        for j in graph[now]:
            cost = dist + j[1]
            
            if distance[j[0]] > cost:
                distance[j[0]] = cost
                heapq.heappush(h, (cost, j[0]))



def solution(n, start, graph):
    distance = [INF] *(n+1)
    
    dijkstra(start, n, distance, graph)

    for i in range(1, n+1):
        if distance[i] == INF:
            print(f"node {start} 에서 node {i} 까지의 최단거리: INFINITY")
        else:
            print(f"node {start} 에서 node {i} 까지의 최단거리: {distance[i]}")

solution(6, 1, [[],[(2,2), (3,5), (4,1)], [(4,2), (3,3)], [(2,3), (6,5)], [(3,3), (5,1)], [(3,1), (6,2)], []])


