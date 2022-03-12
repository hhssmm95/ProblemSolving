def solution(string):
    myset = set(['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='])
    halfset = set(['c', 'd', 'dz', 'l', 'n', 's', 'z'])
    word = ''

    count = 0
    stack = 0

    i=0
    while i < len(string):
        word += string[i]

        if word in halfset and i != len(string)-1:
            stack +=1
            i += 1
            continue

        if stack >= 1 and word not in myset:
            i -=stack

        count +=1
        word = ''
        stack = 0
        i += 1

    return count

string = input()
print(solution(string))


