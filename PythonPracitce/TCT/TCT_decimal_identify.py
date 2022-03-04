import math

def decimal_identify(num):

    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            print(f"{num}은 소수가 아님")
            return
    print(f"{num}은 소수임")

decimal_identify(166)
