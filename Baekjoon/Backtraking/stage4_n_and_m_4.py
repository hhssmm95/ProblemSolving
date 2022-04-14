import sys
input = sys.stdin.readline

def DFS(N, M, array):
    if len(array) >= M:
        for i in array:
            print(i, end = ' ')
        print()
        return

    for i in range(1, N+1):
        if array and array[-1] > i:
                continue
        array.append(i)
        DFS(N,M,array)
        array.pop()


N, M = map(int, input().split())
array = []

DFS(N,M,array)

