import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

def binary_search(target, start, end):
    if start > end:
        return 0

    mid = int((start+end)//2)

    if array[mid] == target:
        return 1

    elif array[mid] > target:
        return binary_search(target, start, mid-1)

    else:
        return binary_search(target, mid+1, end)

array.sort()
for i in nums:
    print(binary_search(i, 0, len(array)-1))

