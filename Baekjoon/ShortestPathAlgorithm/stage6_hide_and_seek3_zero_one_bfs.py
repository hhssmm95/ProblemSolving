from collections import deque
import sys
input = sys.stdin.readline

INF = 1e9
N, K = map(int, input().split())
visited = [INF]*100001

def BFS(start):
    q = deque([start])
    visited[start] = 0

    while q:
        curr = q.popleft()

        if curr * 2 <= 100000 and visited[curr*2] > visited[curr]:
            visited[curr*2] = visited[curr]
            q.appendleft(curr*2)

        if curr + 1 <= 100000 and visited[curr+1] > visited[curr]+1:
            visited[curr+1] = visited[curr]+1
            q.append(curr+1)

        if curr - 1 >= 0 and curr -1 <= 100000 and visited[curr-1] > visited[curr]+1:
            visited[curr-1] = visited[curr]+1
            q.append(curr-1)

BFS(N)
print(visited[K])