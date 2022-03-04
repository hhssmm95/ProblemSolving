def solution(people, limit):
    answer = 0
    
    head = 0
    tail = len(people)-1
    offset = 0
    
    people.sort(reverse = True)
    
    while head <= tail:
        offset = limit - people[tail]
        
        if offset >= people[head]:
            head+=1
            tail-=1
        else:
            head+=1
            
        answer+=1
    

    
    return answer