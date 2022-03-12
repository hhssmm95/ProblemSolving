def solution(string):
    mydict = dict()
    result = []

    for i in range(len(string)):
        if string[i] not in mydict:
            mydict[string[i]] = i
    
    for i in range (ord('a'), ord('z')+1):
        if chr(i) in mydict:
            result.append(mydict[chr(i)])
        else:
            result.append(-1)

    return result

string = input()
result = solution(string)
for i in result:
    print(i, end=' ')
            