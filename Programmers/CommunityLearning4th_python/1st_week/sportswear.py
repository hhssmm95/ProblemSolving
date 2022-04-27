# check N time
def solution1(n, lost, reserve):
    students = [1]*(n+1)

    for i in lost:
        students[i] -= 1
    for i in reserve:
        students[i] += 1

    for i in range(1,n+1):
        if students[i] == 0:
            if i > 1 and students[i-1] == 2:
                students[i] += 1
                students[i-1] -= 1
            elif i < n and students[i+1] == 2:
                students[i] +=1
                students[i+1] -= 1

    return(len([ c for c in students[1:-1] if c > 0]))

# set
def solution2(n, lost, reserve):
    lSet = set(lost) - set(reserve)
    rSet = set(reserve) - set(lost)

    for i in sorted(rSet):
        if i-1 in lSet:
            lSet.remove(i-1)
        elif i+1 in lSet:
            lSet.remove(i+1)
    
    return n-len(lSet)



print(solution2(5, [2,4], [1,3,5]))