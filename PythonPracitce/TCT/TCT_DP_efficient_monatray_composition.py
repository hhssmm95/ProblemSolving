
def solution(N, currencies, M):
    cache = [10001]*(M+1)
    
    cache[0] = 0

    for i in currencies:
        for j in range(i, M+1):
            if cache[j-i] != 10001:
                cache[j] = min(cache[j], cache[j-i] + 1)

    answer = cache[M]
    if answer == 10001:
        return -1
        
    return answer

        # a[i] = min(a[i-k]+1, ai)


print(solution(2, [2,3], 15))