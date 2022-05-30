from collections import defaultdict

def solution(gems):
    answer = []
    gemSet = set(gems)
    gemDict = defaultdict(int)
    shortest = 1e9

    front = 0
    rear = 0
    gemDict[gems[front]]+=1

    while front < len(gems) and rear < len(gems):
        if len(gemDict) == len(gemSet):
            if rear - front < shortest:
                shortest = rear - front
                answer = [front+1, rear+1]

            gemDict[gems[front]]-=1
            if gemDict[gems[front]] <= 0:
                gemDict.pop(gems[front])
            front+=1

        else:
            rear+=1
            if rear<len(gems):
                gemDict[gems[rear]] +=1

    return answer
    
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
#answer 	[3, 7]
'''cases
["AA", "AB", "AC", "AA", "AC"]	[1, 3]
["XYZ", "XYZ", "XYZ"]	[1, 1]
["ZZZ", "YYY", "NNNN", "YYY", "BBB"]	[1, 5]
'''