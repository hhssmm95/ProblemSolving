from collections import deque

def BFS(N,K):
    bfs_queue = deque([(N, '')])
    visited = [0] * 100001

    def insertNext(next, curr, oper):
        if next >= 0 and next <= 100000:
            if visited[next] == 0 or visited[curr] +1 < visited[next]:
                visited[next] = visited[curr] + 1
                bfs_queue.append((next, oper))

    while bfs_queue:
        data = bfs_queue.popleft()
        curr = data[0]
        prev_oper = data[1]

        if curr == K:
            return visited[curr]

        if prev_oper != '-':
            insertNext(curr + 1, curr, '+')
        if prev_oper != '+':
            insertNext(curr - 1, curr, '-')
        insertNext(curr*2, curr, '*')

        


N, K = map(int, input().split())
print(BFS(N,K))
