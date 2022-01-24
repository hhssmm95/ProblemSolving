def euclidFunc(num1, num2):
    if num1 >= num2:
        if num1%num2 == 0:
            return num2
        else:
            return euclidFunc(num2, num1%num2)
    else:
        if num2 % num1 == 0:
            return num1
        else:
            return euclidFunc(num1, num2 % num1)


print(euclidFunc(192, 162))

listt = []
listt.popleft()