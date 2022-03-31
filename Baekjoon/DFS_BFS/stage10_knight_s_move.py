from collections import deque


DR = [2, 2, -2, -2, 1, -1, 1, -1]
DC = [1, -1, 1, -1, 2, 2, -2, -2]

def BFS(N, curr, dest):

    bfs_queue = deque([(curr[0],curr[1])])
    board = [[0] * N for _ in range(N)]

    board[curr[0]][curr[1]] = 0

    while bfs_queue:
        pos = bfs_queue.popleft()
        r = pos[0]
        c = pos[1]

        if pos == dest:
            return board[r][c]

        for i in range(8):
            nr = r + DR[i]
            nc = c + DC[i]
            
            if nr >= 0 and nr < N and nc >= 0 and nc < N:
                if board[nr][nc] == 0:
                    board[nr][nc] = board[r][c] + 1
                    bfs_queue.append((nr,nc))

cases = int(input())

for i in range(cases):
    N = int(input())
    curr = tuple(map(int, input().split()))
    dest = tuple(map(int, input().split()))
    print(BFS(N, curr, dest))

    

