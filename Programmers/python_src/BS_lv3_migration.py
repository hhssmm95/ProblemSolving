def solution(n, times):
    answer = 0

    times.sort()

    #아직 아무도 심사 받지 않았을 때
    start = 0

    #심사가 가장 오래 걸렸을 때
    end = times[-1]*n

    while start <= end:
        mid = (start + end) //2

        processed = 0

        for t in times:
            processed += mid // t

        if processed >= n:
            end = mid-1

        else:
            start = mid+1
    
    answer = end+1



    return answer