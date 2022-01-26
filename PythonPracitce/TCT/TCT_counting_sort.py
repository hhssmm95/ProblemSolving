def counting_sort(nums, reverse = False):

    cIndex = [0]* (max(nums)+1)
    
    for i in nums:
        cIndex[i]+=1

    result = []

    for i in range(len(cIndex)):
        for j in range(cIndex[i]):
            result.append(i)

    if reverse:
        result.reverse()
    
    return result

print(counting_sort([5,7,9,0,3,1,6,2,4,8,1,5,6,3,5,7,2,1,8,9]))

