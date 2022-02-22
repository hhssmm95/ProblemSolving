def solution(n, soldiers):
    dp = [1] * (n+1)

    soldiers.reverse()

    for i in range(1,n):
        for j in range(0, i):
            if soldiers[j] < soldiers[i]:
                dp[i] = max(dp[i], dp[j] +1)
    return n-max(dp)


    #LIS (Longest Increasing Subsequence) : 가장 긴 증가하는 부분수열 알고리즘에 따라
    # (1 <= j < i) dp[i] = max(dp[i], dp[j]+1) if array[j] < array[i]

    #가장 긴 감소하는 부분 수열 구하기
    # (2000 >= j > i >= 1)  dp[i] = max(dp[i], dp[j]+1) if array[j] > array[i]

    #혹은 배열 반전 후 증가하는 부분 수열 구한 후 전체 길이와의 차 구하기

print(solution(7, [15,11,4,8,5,2,4]))