from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    reportDict = defaultdict(set)
    resultDict = defaultdict(int)

    for rep in report:
        reporter, target = rep.split()
        reportDict[target].add(reporter)
        
    for rSet in reportDict.values():
        if len(rSet) >= k:
            for reporter in rSet:
                resultDict[reporter]+=1

    for id in id_list:
        answer.append(resultDict[id])
    
    return answer

print(solution(["con", "ryan"],	["ryan con", "ryan con", "ryan con", "ryan con"],	3))

'''cases
["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2
["con", "ryan"]	["ryan con", "ryan con", "ryan con", "ryan con"]	3
'''