min_count = 9
cache = []

def DP(N, x, target):
    # N*count 형식의 숫자부터 삽입 ex) N=5, count=4 -> 5555
    cache[x].append(int(str(N)*x))
    #최소값이 x일때 DP(x)의 모든 연산결과 = 1 + (DP(i) + DP(x-i)) + (DP(i) - DP(x-i)) + (DP(i) * DP(x-i)) + (DP(i) // DP(x-i))
    for i in range(1,x):
        #같은 연산이 계속 중복되므로 값을 저장해두었다 계속 꺼내서 쓸 수 있는 cache 활용
        #cache[i]가 비어있으면 DP(i)를 통해 cache[i]를반환받음
        for op1 in cache[i] if cache[i] else DP(N,i,target):
            for op2 in cache[x - i] if cache[x - i] else DP(N,x - i,target):
                cache[x].append(op1+op2)
                cache[x].append(op1-op2)
                cache[x].append(op1*op2)
                if op2 > 0:
                    cache[x].append(op1//op2)

    #위 연산으로 cache[x]에 모든 연산결과가 담겼고, target이 포함되어 있는지 확인
    if target in cache[x]:
        global min_count
        min_count = min(min_count, x)

    #탑 다운 형식으로 계속해서 깊은 곳으로 재귀되기 때문에 최소x를 찾을 수 있음
    return cache[x]

def solution(N, number):
    answer = 0

    # 최소값이 x일때의 모든 연산 결과를 담기위한 배열 cache 생성
    global cache
    cache = [[] for _ in range(9)]

    # 탑다운 DP
    DP(N,8, number)

    return min_count if min_count < 9 else -1

print(solution(5, 31168))