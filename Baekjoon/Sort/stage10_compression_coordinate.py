import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
mySet = set(array)

sorted_array = sorted(list(mySet))
compMap = dict()
for i in range(len(sorted_array)):
    compMap[sorted_array[i]] = i


for i in array:
    print(compMap[i], end=' ')
print()