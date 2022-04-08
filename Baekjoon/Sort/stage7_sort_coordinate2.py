from functools import cmp_to_key 
import sys
input = sys.stdin.readline


def cmp_custom(a, b):
    if a[1] < b[1]:
        return -1
    elif a[1] == b[1]:
        if a[0] < b[0]:
            return -1
        else:
            return 1
    else:
        return 1
        

N = int(input())
array = []
for i in range(N):
    array.append(tuple(map(int, input().split())))
array.sort(key=cmp_to_key(cmp_custom))

for i in array:
    print(f'{i[0]} {i[1]}')