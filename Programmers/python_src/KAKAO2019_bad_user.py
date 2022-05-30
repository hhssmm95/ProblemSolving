from itertools import permutations

def checkPermutation(user_perm, banned_id):
    for idx in range(len(banned_id)):
        if len(user_perm[idx]) != len(banned_id[idx]):
            return False

        for i in range(len(banned_id[idx])):
            if banned_id[idx][i] != user_perm[idx][i] and banned_id[idx][i] != '*':
                return False

    return True

def solution(user_id, banned_id):
    answerList = []
    user_perm = list(permutations(user_id, len(banned_id)))
    
    for perm in user_perm:
        if checkPermutation(perm, banned_id):
            sPerm = set(perm)
            if sPerm not in answerList:
                answerList.append(sPerm)

    return len(answerList)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))