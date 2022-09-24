def solution(stones, k):
    answer = 0

    start = 1
    end = 200000000

    while start<=end:
        mid = (start+end)//2

        new_stones = [s - mid for s in stones]
        max_cnt = 0
        cnt = 0
        for ns in new_stones:
            if ns < 0:
                cnt+=1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 0

        #answer = mid

        if max_cnt >= k:
            end = mid-1
        else:
            start = mid+1
            
    answer = end

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],	3))