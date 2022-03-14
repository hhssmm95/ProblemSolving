def solution(floor, room):
    apartment = [[0]* (room+1) for _ in range(floor+1)]

    for i in range(1, room+1):
        apartment[0][i] = i

    for i in range(1, floor):
        for j in range(1, room+1):
            apartment[i][j] = sum(apartment[i-1][1:j+1])

    return sum(apartment[floor-1][1:room+1])


cases = int(input())

for i in range(cases):
    floor = int(input()) 
    room = int(input())

    print(solution(floor, room))



    