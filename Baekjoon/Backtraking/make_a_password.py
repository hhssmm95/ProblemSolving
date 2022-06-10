import sys
input = sys.stdin.readline

L,C = map(int, input().split())
chars = list(input().split())
chars.sort()

vowels = {'a','e','i','o','u'}
def DFS(idx, password, length, cCount,vCount):
    if length == L:
        if cCount >= 2 and vCount >= 1:
            print(password)
            return True
        else:
            return False
    elif (C-idx+1) <(L-length):
        return False

    for i in range(idx, C - (L - length)+1):
        if chars[i] in vowels:
            DFS(i+1, password + chars[i], length+1, cCount, vCount+1)
        else:
            DFS(i+1, password + chars[i], length+1, cCount+1, vCount)
    return False


DFS(0,"",0,0,0)
        


    
