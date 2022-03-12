def solution(num1, num2):
    int1 = int(num1[2])*100 + int(num1[1])*10 + int(num1[0])
    int2 = int(num2[2])*100 + int(num2[1])*10 + int(num2[0])

    if int1 > int2:
        return int1
    else:
        return int2

num1, num2 = input().split()
print(solution(num1, num2))

    