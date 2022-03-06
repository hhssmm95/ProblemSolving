from collections import deque

def topological_sort(v,e, edges):
    indegree = [0] * (v+1)
    graph = [[] for i in range (v+1)]
    result = []

    for i in edges:
        graph[i[0]].append(i[1])
        indegree[i[1]]+=1
    
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        result.append(node)

        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)


    print(result, end=' ')

topological_sort(7, 8, [(1,2), (1,5), (2,3), (2,6), (3,4), (4,7), (5,6), (6,4)])