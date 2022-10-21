def solution(a):
    answer = 2

    rear = [int(1e9)] * len(a)
    rear_min = int(1e9)
    for i in range(len(a)-1,-1,-1):
        rear_min = min(rear_min, a[i])
        rear[i] = rear_min
        

    front_min = a[0]

    for i in range(1,len(a)-1):
        rear_min = rear[i+1]
        if front_min > a[i] or rear_min > a[i]:
            answer+=1
        front_min = min(front_min, a[i])

    return answer

print(solution([9,-1,-5]))
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))