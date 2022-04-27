
def solution(number, k):
    stack = []
    for idx, num in enumerate(number):
        if not stack:
            stack.append(num)
            continue
        if k >0:
            while stack[-1] < num:
                stack.pop()
                k-=1
                if k <= 0 or not stack:
                    break
        stack.append(num)

    return ''.join(stack[:-k] if k else stack)


print(solution("4177252841", 4)) 