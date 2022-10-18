# def solution(s):
#     answer = 0
#     ans_str = ''
#     for i in range(len(s)):
#         head = i
#         tail = len(s)-1
#         length = 0
#         while head <= tail:
#             if s[head]==s[tail]:
#                 if head == tail:
#                     length +=1
#                 else:
#                     length+=2

#                 head+=1

#             elif head > i:
#                 head = i
#                 length = 0

#                 if s[head]==s[tail]:
#                     if head == tail:
#                         length +=1
#                     else:
#                         length+=2

#                     head+=1
#             tail-=1

#         if answer < length:
#             ans_str = s[i:i+length]
#         answer = max(answer,length)
#     print(ans_str)
#     return answer

def solution(s):
    answer = 0
    ans_str = ''

    for i in range(len(s)):
        head = i-1
        tail = i+1


        if tail < len(s) and s[i] == s[tail]:
            length = 2
            tail+=1
            while head >= 0 and tail < len(s) and s[head] == s[tail]:
                length += 2
                head-=1
                tail+=1
            answer = max(answer,length)
            
        
        head = i-1
        tail = i+1
        length = 1

        while head >= 0 and tail < len(s) and s[head] == s[tail]:
            length += 2
            head-=1
            tail+=1

        if answer < length:
            ans_str = s[i:i+length]
        answer = max(answer,length)

    print(ans_str)
    return answer

#print(solution('BBBBBBBBBBBBBBBBBABBBBBBBBBBBBBBBBBB'))
print(solution("aaaa"))