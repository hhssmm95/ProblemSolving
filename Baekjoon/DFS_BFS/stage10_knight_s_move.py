from collections import deque


R = [1, -1, 0, 0]
C = [0, 0, 1, -1]
D = [[(1,1), (1,-1)], [(-1,1), (-1,-1)], [(1,1), (-1,1)], [(1, -1), (-1, -1)]]
DR = [1, 1, -1, -1, 1, -1, 1, -1]
DC = [1, -1, 1, -1, 1, 1, -1, -1]

def BFS(N, curr, dest):

    bfs_queue = deque([(curr[0],curr[1])])
    board = [[0] * N for _ in range(N)]
    board[curr[0], curr[1]] = 1

    while bfs_queue:
        pos = bfs_queue.popleft()
        r = pos[0]
        c = pos[1]

        if pos == dest:
            return board[r][c]

        for i in range(8):
            nr = r + DR[i]
            nc = c + DC[i]

            if board[nr][nc] == 0:
                board[nr][nc] = board[r][c] + 1
                bfs_queue.append((r,c))

cases = int(input())

for i in range(cases):
    N = int(input())
    curr = tuple(map(int, input().split()))
    dest = tuple(map(int, input().split()))
    print()

    

