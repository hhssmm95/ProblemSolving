import sys
input = sys.stdin.readline

array = list(map(int, input().rstrip()))
print(''.join(map(str,sorted(array, reverse=True))))


