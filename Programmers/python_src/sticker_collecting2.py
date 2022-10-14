#맨 앞을 뜯는지 않뜯는지로 구분하여 DP진행

def solution(sticker):
    N = len(sticker)

    if N == 1:
        return sticker[0]

    #cache1 : 맨 앞 뜯음, cache2 : 안뜯음
    cache1, cache2 = [0]*N, [0]*N

    cache1[0] = sticker[0]
    cache1[1] = cache1[0]

    for i in range(2, N-1):
        cache1[i] = max(cache1[i-2] + sticker[i], cache1[i-1])

    for j in range(1,N):
        cache2[j] = max(cache2[j-2] + sticker[j], cache2[j-1])

    return max(cache1[-2], cache2[-1])

print(solution([1,3,2,5,4]))
#print(solution([14, 6, 5, 11, 3, 9, 2, 10]))