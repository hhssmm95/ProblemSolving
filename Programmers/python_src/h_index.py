def solution(citations):
    answer = 0

    citations.sort(reverse = True)

    if citations[0] == 0:
        return 0


    for i in range(1,len(citations)+1):
        if citations[i-1] >= i:
            answer = i
        

    return answer