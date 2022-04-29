from itertools import permutations, combinations, product, combinations_with_replacement
from collections import deque,defaultdict
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
array = list(map(int, input().split()))
prefix_sum = [0]

for i in range(N):
    prefix_sum.append(prefix_sum[-1] + array[i])

left = 1
right = 1

shortest = 1e9+1

while left<=N:
    if prefix_sum[right] - prefix_sum[left-1] >= S:
        if right-left+1 < shortest:
            shortest = right-left+1
        left+=1
    else:
        if right != N:
            right+=1
        else:
            left+=1
print(shortest if shortest < 1e9+1 else 0)