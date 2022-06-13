from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int,input().split()))
res = []

def search_and_insert(num):
    if not res or res[-1] < num:
        res.append(num)
    else:
        res[bisect_left(res,num)] = num
for seq_num in seq:
    search_and_insert(seq_num)

print(len(res))
