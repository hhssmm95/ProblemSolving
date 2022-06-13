from bisect import bisect_left
import sys
input = sys.stdin.readline

x,y,c = map(float, input().split())

def cal(x,y,w):
    h1 = (x**2 - w**2)**0.5
    h2 = (y**2 - w**2)**0.5

    c = (h1*h2) / (h1+h2)

    return c

left , right = 0, min(x,y)

while abs(left - right) > 1e-6:
    mid = (left + right) /2.0

    if cal(x,y,mid) > c:
        left = mid #cal의 return은 w에 반비례
    else:
        right = mid

print(round(mid,3))

