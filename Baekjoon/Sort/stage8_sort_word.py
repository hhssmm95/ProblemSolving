from functools import cmp_to_key 
import sys
input = sys.stdin.readline


def cmp_custom(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) == len(b):
        if a < b:
            return -1
        else:
            return 1
    else:
        return 1
        

N = int(input())

myset = set()
for i in range(N):
    myset.add(input())

array = []
for i in myset:
    array.append(i)

array.sort(key=cmp_to_key(cmp_custom))

for i in array:
    print(i, end='')