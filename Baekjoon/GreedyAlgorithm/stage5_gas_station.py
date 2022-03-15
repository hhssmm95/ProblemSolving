def solution(N, distances, costs):
    now = 0
    next = 0

    result = 0
    dist_idx = 0

    for i in range(1, len(costs)):
        result += (distances[dist_idx] * costs[now])

        next = i
        if costs[now] >= costs[next]:
            now = next
        dist_idx+=1

    return result

N = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))
print(solution(N, distances, costs))