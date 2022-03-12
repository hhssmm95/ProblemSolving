def solution(num):
    count = 1
    mult = 0
    offset = 1
    while True:
        if num <= (6 * mult) +1:
            return count
        mult+=offset
        offset+=1
        count+=1

num = int(input())
print(solution(num))
