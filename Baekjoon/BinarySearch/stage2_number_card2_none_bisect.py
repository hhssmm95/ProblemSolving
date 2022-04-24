import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
counting_nums = list(map(int, input().split()))

cards.sort()


def bisect_left(start, end, num):
    while start<=end:
        mid = (start + end) //2

        if cards[mid] >= num:
            end = mid-1
        else:
            start = mid+1
    return start

def bisect_right(start, end, num):
    while start<=end:
        mid = (start + end) //2

        if cards[mid] > num:
            end = mid-1
        else:
            start = mid+1
    return start

for i in counting_nums:
    print(bisect_right(0, N-1, i) - bisect_left(0,N-1,i), end = ' ')
print()
