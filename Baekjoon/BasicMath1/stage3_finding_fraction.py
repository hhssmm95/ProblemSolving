def solution(seq):
    
    num = 0
    stage = 1
    
    denominator = 0
    numerator = 0

    while True:
        num += stage
        if seq <= num:
            if stage %2 == 0:
                  denominator = 1 + abs(num - seq)
                  numerator = stage - abs(num - seq)
            else:
                denominator =  stage - abs(num - seq)
                numerator = 1 + abs(num - seq)
            break

        stage+=1
    
    return f"{numerator}/{denominator}"

seq = int(input())
print(solution(seq))
                