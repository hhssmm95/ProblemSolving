def solution(number, k):
    cmp_stack = []

    for num in number:
        if not cmp_stack:
            cmp_stack.append(num)
            continue
        if k>0:
            while cmp_stack[-1] < num:
                cmp_stack.pop()
                k-=1

                if k<=0 or not cmp_stack:
                    break
        cmp_stack.append(num)

    return ''.join(cmp_stack[:len(cmp_stack)-k])

print(solution("4177252841", 4))