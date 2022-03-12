def solution(word):
    myset = set()

    current_char = ''
    for i in word:
        if current_char == i:
            continue

        if i in myset:
            return False

        myset.add(current_char)
        current_char = i
    return True

result = 0
n = int(input())

for i in range(n):
    word = input()
    if solution(word):
        result += 1
print(result)


        
