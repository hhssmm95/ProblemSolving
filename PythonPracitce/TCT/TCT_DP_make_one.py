def solution(number):
    cache = [0] * 30001

    for i in range(2, number+1):
        cache[i] = cache[i-1] +1

        if i % 2 == 0:
            cache[i] = min(cache[i], cache[i//2] + 1)
        if i % 3 == 0:
            cache[i] = min(cache[i], cache[i//3] + 1)
        if i % 5 == 0:         
            cache[i] = min(cache[i], cache[i//5] + 1)

    


    answer = cache[number]

    return answer

print(solution(26))