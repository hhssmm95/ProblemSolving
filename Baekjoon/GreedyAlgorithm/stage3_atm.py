def solution(N, costs):
    result = 0
    
    costs.sort()
    
    for i in range(1, len(costs)):
        costs[i] = costs[i-1] + costs[i]

    
    return sum(costs)

N = int(input())
costs = list(map(int, input().split()))
print(solution(N, costs))