import collections

#dictionary
def solution1(participant, completion):
    part_dic = dict()

    for i in participant:
        part_dic[i] = part_dic.get(i, 0) +1
    for i in completion:
        part_dic[i]-=1
    
    result = [k for k,v in part_dic.items() if v>0]

    return result[0]

#hash function
def solution2(participant, completion):
    part_dic = dict()
    hash_tmp = 0

    for p in participant:
        part_dic[hash(p)] = p
        hash_tmp += hash(p)
    
    for c in completion:
        hash_tmp -= hash(c)

    return part_dic[hash_tmp]

#counter
def solution3(participant, completion):
    result = collections.Counter(participant) - collections.Counter(completion)
    return list(result.keys())[0]


#sort
def solution4(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[-1]




print(solution4(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
