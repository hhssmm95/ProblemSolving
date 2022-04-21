import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2

    total = 0
    for len in trees:
        if len - mid >= 0:
            total += len-mid

    if total < M:
        end = mid-1

    elif total >= M:
        start = mid+1
print(end)