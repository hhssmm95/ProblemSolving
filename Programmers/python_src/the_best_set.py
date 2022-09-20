def solution(n, s):
    answer = []
    
    num = s//n
    rest = s%n

    if s < n:
        return [-1]

    for i in range(n):
        if i >= n - rest:
            answer.append(num+1)
        else:
            answer.append(num)
    
    return answer

print(solution(17,50))