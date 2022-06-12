from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cMap = []
cList = []
hList = []
for i in range(N):
    line = list(map(int,input().split()))
    for j, num in enumerate(line):
        if num == 2:
            cList.append((i,j))
        elif num == 1:
            hList.append((i,j))
    cMap.append(line)

answer = int(1e9)
cComb = list(combinations(cList, M))

def getCityChickenMeter(comb):
    CC_Meter = 0
    for hR,hC in hList:
        chickenMeter = int(1e9)
        for cR,cC in comb:
            chickenMeter = min(chickenMeter, abs(hR-cR) + abs(hC-cC))
        CC_Meter += chickenMeter
    return CC_Meter

for comb in cComb:
    answer = min(answer, getCityChickenMeter(comb))


print(answer)
