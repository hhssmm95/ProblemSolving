from operator import ne
import sys
input = sys.stdin.readline

N = int(input())
graph = [[0] for _ in range(N+1)]
answer = int(1e9)

for i in range(1,N+1):
    graph[i] += list(map(int, input().split()))

visited = [False]*(N+1)

def DFS(startNode, currNode, cost, depth):
    if depth == N:
        if graph[currNode][startNode] == 0:
            return
        else:
            global answer
            answer = min(answer, cost + graph[currNode][startNode])
            return

    for neighbor, edge_cost in enumerate(graph[currNode]):
        if visited[neighbor] or edge_cost == 0:
            continue
        visited[neighbor] = True
        DFS(startNode, neighbor, cost + edge_cost, depth+1)
        visited[neighbor] = False

for i in range(1,N+1):
    visited[i] = True
    DFS(i,i,0,1)
    visited[i] = False

print(answer)