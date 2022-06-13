from bisect import bisect_left
import sys
input = sys.stdin.readline

N, H  = map(int, input().split())

ceilHurdle = []
floorHurdle = []

for i in range(N):
    if i % 2 == 0:
        floorHurdle.append(int(input()))
    else:
        ceilHurdle.append(H-int(input()))

floorHurdle.sort()
ceilHurdle.sort()

answer = [int(1e9), 0]

for h in range(1,H+1):
    curr_height = h-0.5
    destroy = N//2 - bisect_left(floorHurdle, curr_height) +  bisect_left(ceilHurdle, curr_height)
    if answer[0] > destroy:
        answer[0] = destroy
        answer[1] = 1

    elif answer[0] == destroy:
        answer[1]+=1
        
print(answer[0], answer[1])




