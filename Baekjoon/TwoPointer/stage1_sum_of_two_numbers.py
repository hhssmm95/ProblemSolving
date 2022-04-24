import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
x = int(input())

head, tail = 0, n-1
count = 0

array.sort()
while head<tail:
    result = array[head]+array[tail]

    if result == x:
        count+=1

    if result > x:
        tail-=1
    else:
        head+=1
print(count)
