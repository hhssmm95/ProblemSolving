from math import ceil

def solution(n, stations, w):
    answer = 0
    area = []
    cover_dist = w*2+1
    
    last_end = 1
    for s in stations:
        new_front = s-w-1
        if new_front >= last_end:
            area.append(abs(new_front - last_end + 1))
        last_end = s+w+1

    if last_end <= n:
        area.append(abs(n-last_end+1))

    for a in area:
        answer += ceil(a/cover_dist)

    return answer