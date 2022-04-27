import sys
input = sys.stdin.readline

N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

min_offset = 2*1e9+1
answer = (-1,-1)
head, tail = 0, N-1

while head < tail:
    sum = solutions[head] + solutions[tail]

    if sum == 0:
        print(f"{solutions[head]} {solutions[tail]}")
        break

    if min_offset > abs(sum):
        min_offset = abs(sum)
        answer = (solutions[head], solutions[tail])

    
    if sum < 0:
        head+=1
    else:
        tail-=1
else:
    print(f"{answer[0]} {answer[1]}")
    