from collections import defaultdict

def union(parent, a, b):
    if b == "-":
        parent[a][0] = "master"
        return
    parent[a][0] = b
    

def sell(parent, s, profit):

    if parent[s][0] == s:
        parent[s][1]+=profit
        return

    bonus = int(profit/10)
    parent[s][1]+=profit - bonus

    if bonus >= 1:
        sell(parent, parent[s][0], bonus)
        

def solution(enroll, referral, seller, amount):
    answer = []

    N = len(enroll)
    M = len(seller)
    parent = defaultdict(list)
    parent["master"] = ["master",0]
    
    for e in enroll:
        parent[e].append(e)
        parent[e].append(0)

    for i in range(N):
        union(parent, enroll[i], referral[i])

    for j in range(M):
        sell(parent, seller[j], amount[j]*100)

    for key in parent.keys():
        if key == "master":
            continue
        answer.append(parent[key][1])

    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))