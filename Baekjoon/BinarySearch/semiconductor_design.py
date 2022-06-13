from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
connect = list(map(int,input().split()))
res = []

def make_LIS(num):
    if not res or res[-1] < num:
        res.append(num)
    else:
        res[bisect_left(res, num)] = num

for c in connect:
    make_LIS(c)

print(len(res))
