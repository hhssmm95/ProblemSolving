import heapq

INF = 1e9

def solution(N, M, C, graph):
    answer = [0, 0]
    distance = [INF] * (N+1)
    dijkstra(N, C, distance, graph)
    
    for i in range(1, N+1):
        if i != C and distance[i] != INF:
            answer[0] += 1
            if distance[i] > answer[1]:
                answer[1] = distance[i]
    return answer


def dijkstra(N, C, distance, graph):
    distance[C] = 0
    q = []

    heapq.heappush(q, (0,C))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        
        for i in graph:
            if i[0] == C:
                cost = dist + i[2]
                if distance[i[1]] > cost:
                    distance[i[1]] = cost
                    heapq.heappush(q, (cost, i[1]))

print(solution(3, 2, 1, [(1,2,4), (1,3,2)]))

    