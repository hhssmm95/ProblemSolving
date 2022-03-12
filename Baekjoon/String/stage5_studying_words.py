def solution(string):

    dic = dict()
    words = string.lower()

    for i in words:
        if i in dic:
             dic[i]+=1
        else:
            dic[i] = 1
    
    key_array = list(dic.keys())
    val_array = list(dic.values())

    max_val = max(val_array)

    if val_array.count(max_val) >= 2:
        return '?'
        

    answer = key_array[val_array.index(max_val)].upper()

    return answer
    

string = input()
print(solution(string))