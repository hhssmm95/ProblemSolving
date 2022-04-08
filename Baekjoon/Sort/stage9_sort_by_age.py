from functools import cmp_to_key 
import sys
input = sys.stdin.readline


def cmp_custom(a, b):
    if int(a[0]) < int(b[0]):
        return -1
    elif int(a[0]) == int(b[0]):
        return 0
    else:
        return 1
        

N = int(input())

array = []
for i in range(N):
    array.append(tuple(input().split()))

array.sort(key=cmp_to_key(cmp_custom))

for i in array:
    print(f'{i[0]} {i[1]}')