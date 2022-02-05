from functools import cmp_to_key

def cmp_func(a, b):
    if int(a+b) >= int(b+a):
        return -1
    else:
        return 1

def solution(numbers):
    str_nums = list(map(str, numbers))
    str_nums.sort(key=cmp_to_key(cmp_func))


    answer = ''.join(str_nums)

    return answer

print(solution([3, 30, 34, 5, 9]))