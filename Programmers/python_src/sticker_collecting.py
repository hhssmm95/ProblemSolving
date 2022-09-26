'''
max_sum = 0
def dfs(index, curr_sum, count, sticker, visited):
    if count >= len(sticker):
        global max_sum
        max_sum = max(max_sum, curr_sum)
        return

    else:
        prev_index = index-1 if index-1>=0 else len(sticker)-1
        next_index = index+1 if index+1 < len(sticker) else 0

        dfs(next_index, curr_sum, count+1, sticker, visited)


        if(prev_index not in visited and next_index not in visited):
            visited.add(index)
            dfs(next_index, curr_sum + sticker[index], count+1, sticker, visited)

    if index in visited:
        visited.remove(index)

def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    for i in range(len(sticker)):
        dfs(i, 0,0, sticker, set())
        
    return max_sum

'''

cache = []
 
def DP(index, sticker):
    p_index = index-1 if index-1>=0 else len(sticker)-1
    pp_index = p_index-1 if p_index-1>=0 else len(sticker)-1

    if cache[index] != -1:
        return cache[index]
        #max(DP)
    result = max(DP(pp_index, sticker) + sticker[index], DP(p_index, sticker))
    cache[index] = max()
    return cache[index]

def solution(sticker):
    global cache
    answer = 0

    for i in range(len(sticker)):
        cache = [-1]*(len(sticker))

        n_index = i+1 if i+1 < len(sticker) else 0
        nn_index = n_index+1 if n_index+1 < len(sticker) else 0

        cache[n_index] = sticker[n_index]
        cache[nn_index] = sticker[nn_index]
        answer = max(answer, DP(max(), sticker))
       
    return answer


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))