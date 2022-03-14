def solution(cdist, fdist, total):
    if (total-cdist) % (cdist-fdist) != 0:
        return ((total-cdist) // (cdist - fdist)) + 2
    else:
        return ((total-cdist) // (cdist - fdist)) + 1

a, b, v = map(int, input().split(' '))
print(solution(a,b,v))