import sys
input = sys.stdin.readline

N = int(input())

counter = [0] * 10001

for i in range(N):
    counter[int(input())] += 1

for i in range(1, 10001):
        for j in range(counter[i]):
            print(i)