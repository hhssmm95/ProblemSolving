def insertion_sort(nums, reverse = False):
    if not reverse:
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                else:
                    break
    else:
        for i in range(1, len(nums)):
            target_idx = i
            for j in range(i, 0, -1):
                if nums[j] > nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                else:
                    break
    return nums


print(insertion_sort([7,5,9,0,3,1,6,2,4,8], reverse=True))