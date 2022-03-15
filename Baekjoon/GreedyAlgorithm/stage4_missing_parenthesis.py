def solution(string):
    nums =[]
    symbols = []

    temp = ''
    for i in range(len(string)):
        if string[i] != '+' and string[i] != '-':
            temp += string[i]

            if i == len(string)-1:
                nums.append(int(temp))
        else:
            nums.append(int(temp))
            symbols.append(string[i])
            temp = ''
    
        
    if '-' in symbols:
        start_idx = symbols.index('-') + 1
    else:
        return sum(nums)
        
    minus_num = sum(nums[start_idx:])
    plus_num = sum(nums[0:start_idx])

    return plus_num - minus_num

string = input()
print(solution(string))
    