def solution(numbers):
    array = list(map(int, numbers))

    return sum(array)

n = input()
numbers = input()
print(solution(numbers))