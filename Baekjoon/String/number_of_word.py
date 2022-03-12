def solution(string):
    array = string.split(' ')
    return len(array) - array.count('')

string = input()
print(solution(string))