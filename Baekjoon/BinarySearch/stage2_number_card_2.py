import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

array.sort()
for i in nums:
    result = bisect_right(array, i) - bisect_left(array, i)
    print(result, end = ' ')
print()