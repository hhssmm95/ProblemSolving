def solution(rtime, string):
    result = ''

    for i in string:
        for j in range(rtime):
            result+=i

    return result

cases = int(input())
for i in range(cases):
    s_rtime, string = input().split()
    rtime = int(s_rtime)
    print(solution(rtime, string))
    