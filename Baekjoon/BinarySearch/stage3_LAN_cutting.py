import sys
input = sys.stdin.readline

K, N = map(int, input().split())
LANs = []

for _ in range(K):
    LANs.append(int(input()))

LANs.sort()

def binary_search(N, start, end):
    if end - start <= 1:
        print(end)
        return

    mid = (start + end) //2

    total = 0
    for len in LANs:
        total += (len // mid)

    if total < N:
        binary_search(N, start, mid-1)

    elif total >= N:
        binary_search(N, mid+1, end)

max_len = len(LANs)-1
binary_search(N,0,LANs[max_len])
    