import sys
input = sys.stdin.readline

N,K = map(int, input().split())

w = [0]*(N+1)
v = [0]*(N+1)
cache = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    w[i], v[i] = map(int,input().split())

for j in range(1,K+1):
    for i in range(1,N+1):
        if j-w[i] < 0:
            cache[i][j] = cache[i-1][j]
        else:
            cache[i][j] = max(cache[i-1][j], cache[i-1][j-w[i]] + v[i])

print(cache[N][K])

    