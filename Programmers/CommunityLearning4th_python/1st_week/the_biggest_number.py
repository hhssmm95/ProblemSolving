from functools import cmp_to_key 

#using lambda
def solution1(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x : x*3, reverse=True)
    if numbers[0] == '0':
        return '0'
    return ''.join(numbers)

#using cmp_to_keys
def cmp_custom(a, b):
    str_a = str(a)
    str_b = str(b)

    if int(str_a + str_b) >= int(str_b + str_a):
        return -1
    else:
        return 1

def solution2(numbers):
    answer = ''
    numbers.sort(key = cmp_to_key(cmp_custom))
    if numbers[0] == 0:
        return "0"

    return ''.join(map(str,numbers))



print(solution2([3, 30, 34, 5, 9])) 