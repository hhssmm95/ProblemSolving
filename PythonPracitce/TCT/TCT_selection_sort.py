def selection_sort(nums, reverse = False):
    if not reverse:
        for i in range(len(nums)-1):
            min_idx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i] , nums[min_idx] = nums[min_idx] , nums[i]
    else:
        for i in range(len(nums)-1):
            max_idx = i
            for j in range(i+1, len(nums)):
                if nums[j] > nums[max_idx]:
                    max_idx = j
            nums[i] , nums[max_idx] = nums[max_idx], nums[i]

    return nums

print(selection_sort([7,5,9,0,3,1,6,2,4,8], reverse = True))
