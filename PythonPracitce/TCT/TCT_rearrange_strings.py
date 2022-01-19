
def solution(string):
    answer = ""
    num = 0
    str_ = []
    for i in string:
        if ord(i) >= ord('A') and ord(i) <= ord('Z'):
            str_.append(i)
        else:
            num += int(i)
    
    str_.sort()
    answer = "".join(str_) + str(num)




    return answer

print(solution('AJKDLSI412K4JSJ9D'))