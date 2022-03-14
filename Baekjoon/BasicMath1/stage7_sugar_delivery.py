def solution(weight):
    count = 0

    while weight>0:
        if weight % 5 == 0:
            count += (weight // 5)
            return count
        else:
            weight -= 3
            count += 1
    
    if weight < 0:
        return -1
            
    
    return count

weight = int(input())
print(solution(weight))
