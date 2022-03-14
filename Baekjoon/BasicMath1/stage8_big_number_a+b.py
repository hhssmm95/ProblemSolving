def solution(a, b):
    result = []

    n = 0

    if len(a) >= len(b):
        n = len(a)
        c = ''
        for i in range(len(a) - len(b)):
            c += '0'
        b = c + b
    
    else:
        n = len(b)
        c = ''
        for i in range(len(b) - len(a)):
            c += '0'
        a = c + a


    i = n-1

    while i>=0:
        if len(result) < n - i:
            result.insert(0, 0)
        
        A = int(a[i])
        B = int(b[i])


        if A + B >= 10:
            result[0] += (A + B - 10)
            result.insert(0, 1)

            if result[1] >= 10:
                result[0] += 1
                result[1] -= 10

        else:
            result[0] += (A + B)

            if result[0] >= 10:
                result.insert(0, 1)
                result[1] -= 10

        i-=1
    
    return "".join(map(str,result))

a,b = input().split(' ')
print(solution(a,b))