import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []

for _ in range(N):
    houses.append(int(input()))

houses.sort()

start, end = 0, houses[-1] - houses[0] #최소간격, 최대간격
answer = -1

while start <= end:
    mid = (start + end) //2 # mid는 공유기 사이의 간격

    set_count = 1

    front = houses[0]
    min_offset = 1e9 # 현재 mid 기준에서 공유기간 가장 인접한 거리

    for i in range(1, N):
        back = houses[i]
        offset = back - front
        if  offset>= mid:
            set_count+=1
            front = back
            min_offset = min(min_offset, offset)


    if set_count < C:
        end = mid-1
    elif set_count >= C:
        start = mid+1
        answer = max(answer, min_offset) # 가장 인접한 공유기간 거리 중에서 나올 수 있는 최대값

print(answer)