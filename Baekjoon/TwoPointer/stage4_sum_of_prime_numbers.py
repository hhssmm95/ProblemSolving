import math
from itertools import permutations, combinations, product, combinations_with_replacement
from collections import deque,defaultdict
import sys
input = sys.stdin.readline

N = int(input())

def eratosthenes(num):
    array = [True] * (num+1)
    result = [0]

    for i in range(2, int(math.sqrt(num)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= num:
                array[i*j] = False
                j+=1

    for i in range(2, num+1):
        if array[i]:
            result.append(result[-1] + i)

    return result
prefix_pSum = eratosthenes(N)
end = len(prefix_pSum)
left, right = 1,1
answer = 0

while left<end:
    if prefix_pSum[right] - prefix_pSum[left-1] > N:
        left+=1
    elif prefix_pSum[right] - prefix_pSum[left-1] == N:
        answer+=1
        left+=1
    else:
        if right != end-1:
            right+=1
        else:
            left+=1

print(answer)