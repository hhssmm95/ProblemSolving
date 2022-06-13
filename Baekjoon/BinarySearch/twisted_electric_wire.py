from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N = int(input())
pilars = list(map(int, input().split()))

res = []

def search_and_insert(num):
    if not res or res[-1] < num:
        res.append(num)
    else:
        res[bisect_left(res,num)] = num
for seq_num in pilars:
    search_and_insert(seq_num)

print(N-len(res))
