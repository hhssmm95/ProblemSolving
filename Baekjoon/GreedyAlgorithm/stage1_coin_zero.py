def solution(N, K, coins):
    coins.reverse()

    count = 0
    
    for i in coins:
        if K % i == 0:
            return count + (K//i)

        while K > i:
            K -= i
            count+=1

    return count

N, K = map(int, input().split(' '))
coins = []

for i in range(N):
    coins.append(int(input()))

print(solution(N, K, coins))