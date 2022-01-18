def solution(N):
    answer = 0

    for hour in range(N+1):
        hr = str(hour)
        for minute in range(60):
            min = str(minute)
            for second in range(60):
                sec = str(second)

                if '3' in hr or '3' in min or '3' in sec:
                    answer+=1

    

    return answer

print(solution(5))