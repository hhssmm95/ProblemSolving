from functools import cmp_to_key

def solution(N, times):

    times.sort(key=lambda x:(x[1], x[0]))
    count = 1

    end_time = times[0][1]
    for i in range(1, len(times)):
        if times[i][0] >= end_time:
            count+=1
            end_time = times[i][1]

    return count

N = int(input())
times = []
for i in range(N):
    times.append(tuple(map(int, input().split(' '))))
print(solution(N, times))