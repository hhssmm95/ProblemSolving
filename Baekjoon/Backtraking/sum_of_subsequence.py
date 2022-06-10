import sys
input = sys.stdin.readline

N,S = map(int, input().split())
seq = list(map(int,input().split()))

answer = 0

def DFS(idx, pSum):
    global answer
    
    if idx >= N:
        return
    pSum += seq[idx]
    if pSum == S:
        answer +=1

    DFS(idx+1, pSum)
    DFS(idx+1, pSum-seq[idx])

DFS(0,0)
print(answer)
