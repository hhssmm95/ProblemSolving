def solution(fixed, variable, profit):
    if variable >= profit:
        return -1
    
    net = profit - variable
    return (fixed // net) +1

fixed, variable, profit = map(int, input().split(' '))
print(solution(fixed, variable, profit))