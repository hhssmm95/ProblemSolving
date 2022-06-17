'''
jump(r,c) = jump(r + dist, c) || jump(r, c + dist)
'''
import sys
input = sys.stdin.readline

n = int(input())
jumpMap = []
for i in range(n):
    jumpMap.append(list(map(int, input().split())))

visited = [[-1] * n for _ in range(n)]

def jump(r,c):
    if (r < 0 or r >= n) or (c < 0 or c >= n):
        return 0
    if (r,c) == (n-1, n-1):
        return 1
    if visited[r][c] != -1:
        return visited[r][c]

    dist = jumpMap[r][c]
    visited[r][c] = jump(r+dist,c) or jump(r,c+dist)
    return visited[r][c]

answer = jump(0,0)
print(answer)