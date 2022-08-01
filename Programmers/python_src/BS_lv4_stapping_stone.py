def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)

    start = 1
    end = distance

    while start<=end:
        mid = (start+end)//2

        del_count = 0
        prev = 0
        
        min_dist = int(1e9)
        for rock in rocks:
            if rock - prev < mid:
                del_count+=1
            else:
                min_dist = min(min_dist, rock - prev)
                prev = rock

        
        if del_count > n:
            end = mid-1

        else:
            start = mid+1
            answer = min_dist

    return answer

print(solution(25,[2, 14, 11, 21, 17],2))