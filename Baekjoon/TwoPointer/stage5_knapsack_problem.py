from itertools import permutations, combinations, product, combinations_with_replacement
from collections import deque,defaultdict
import sys, math
input = sys.stdin.readline

N, C = map(int, input().split())
weights = list(map(int, input().split()))

weights_A = weights[:N//2]
weights_B = weights[N//2:]

def brute_force(weights_sum, weights_part, idx, sum):
    if idx >= len(weights_part):
        weights_sum.append(sum)
        return
    
    brute_force(weights_sum, weights_part, idx+1, sum)
    brute_force(weights_sum, weights_part, idx+1, sum + weights_part[idx])

def binary_seach(weights_sum, target, start, end):
    while start <= end:
        mid = (start + end)//2

        if target -  weights_sum[mid] >= 0:
            start = mid+1
        else:
            end = mid-1
    return start

weights_sumA = []
weights_sumB = []
brute_force(weights_sumA, weights_A, 0, 0)
brute_force(weights_sumB, weights_B, 0, 0)

weights_sumB.sort()
answer = 0
for i in weights_sumA:
    if C - i < 0:
        continue

    answer += binary_seach(weights_sumB, C-i, 0, len(weights_sumB)-1)

print(answer)
