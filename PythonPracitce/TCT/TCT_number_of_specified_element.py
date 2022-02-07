from bisect import bisect_left, bisect_right

def solution(numbers, x):
    result = bisect_right(numbers, x) - bisect_left(numbers,x)

    if result == 0:
        return -1

    return result

print(solution([1,1,2,2,2,2,3], 2))


