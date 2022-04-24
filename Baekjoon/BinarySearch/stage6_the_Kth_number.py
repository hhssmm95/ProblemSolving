import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

start, end = 1, N*N #

while start <= end:
    mid = (start + end) // 2 

    total = 0
    for i in range(1, N+1):
        total += min(mid // i, N) 
        # mid보다 작은 수의 개수는 1x1, 1x2, 1x3, 2x1, 2x2, 3x1인데 그 수는 mid를 각 행으로 나눈 몫의 합에 해당한다
        # 또한 예를들어 mid가 5일 때 5보다 작은 수가 1x1, 1x2, 1x3, 1x4이더라도 4는 N*N 행렬을 벗어난 범위이기 때문에
        #한 행에서 mid보다 작은 수가 N개 보다 클 수는 없으므로 최대값을 N으로 제한한다.
    #total은 모든 행에서의 mid보다 작은 수의 개수의 합이며 total이 3이라면 mid는 적어도 4번째부터의 수에 해당한다.
    if total < k:
        start = mid+1
    elif total  >= k:
        end = mid-1
print(start)


    

