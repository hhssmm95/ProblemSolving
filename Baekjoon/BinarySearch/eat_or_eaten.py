from bisect import bisect_left
import sys
input = sys.stdin.readline

case = int(input())

for c in range(case):
    N,M = map(int, input().split())
    seqA = list(map(int,input().split()))
    seqB = list(map(int,input().split()))

    seqA.sort()
    seqB.sort()

    answer = 0

    for a in seqA:
        answer += bisect_left(seqB, a)
    
    print(answer)

