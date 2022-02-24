INF = 1e9

def get_smallest_node(n, distance, visited):
    small_val = INF
    index = 0

    for i in range(1,n+1):
        if visited[i] == False and distance[i] < small_val:
            small_val = distance[i]
            index = i

    return index

def dijkstra(start, n, distance, visited, graph):
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1]

    for i in range(n-1):
        now = get_smallest_node(n, distance, visited)
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            
            if distance[j[0]] > cost:
                distance[j[0]] = cost



def solution(n, start, graph):
    visited = [False]*(n+1)
    distance = [INF] *(n+1)
    
    dijkstra(start, n, distance, visited, graph)

    for i in range(1, n+1):
        if distance[i] == INF:
            print(f"node {start} 에서 node {i} 까지의 최단거리: INFINITY")
        else:
            print(f"node {start} 에서 node {i} 까지의 최단거리: {distance[i]}")

solution(6, 1, [[],[(2,2), (3,5), (4,1)], [(4,2), (3,3)], [(2,3), (6,5)], [(3,3), (5,1)], [(3,1), (6,2)], []])


