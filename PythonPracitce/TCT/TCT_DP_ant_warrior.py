def DP(x, cargoes, cache):
    if x == 0:
        return cargoes[0]
    elif x == 1:
        return max(cargoes[0], cargoes[1])

    nearCase = 0
    farCase = 0

    if cache[x-1] == 0:
        cache[x-1] = DP(x-1, cargoes, cache)
        nearCase = cache[x-1]
    else:
        nearCase = cache[x-1]
    
    if cache[x-2] == 0:
        cache[x-2] = DP(x-2, cargoes, cache)
        farCase = cache[x-2] + cargoes[x]
    else:
        farCase = cache[x-2] + cargoes[x]

    return max(nearCase, farCase)




def solution(cargoes):
    #a[i] = max(a[i-1], a[i-2]+c[i])
    cache = [0] * len(cargoes)
    answer = DP(len(cargoes)-1, cargoes, cache)

    return answer

print(solution([1,3,1,5]))