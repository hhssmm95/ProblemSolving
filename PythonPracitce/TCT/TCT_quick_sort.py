def quick_sort(nums, start, end, reverse = False):
    if start >= end:
        return

    pivot = start
    left = start+1
    right = end

    if not reverse:
        while (left<=right):
            while (left <= end and nums[left] <= nums[pivot]):
                left+=1
            while (right > start and nums[right] >= nums[pivot]):
                right-=1
            
            if left > right:
                nums[pivot], nums[right] = nums[right], nums[pivot]
            else:
                nums[left], nums[right] = nums[right], nums[left]

        quick_sort(nums, start, right-1)
        quick_sort(nums, right+1, end)

    else:
        while left<=right:
            while nums[left] >= nums[pivot] and left <= end:
                left+=1
            while nums[right] <= nums[pivot] and right > start:
                right-=1
            
            if left > right:
                nums[pivot], nums[right] = nums[right], nums[pivot]
            else:
                nums[left], nums[right] = nums[right], nums[left]

        quick_sort(nums, start, right-1, True)
        quick_sort(nums, right+1, end, True)
        

def short_quick_sort(nums, reverse = False):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    tail = nums[1:]
    
    if not reverse:
        front = [x for x in tail if x <= pivot]
        rear = [x for x in tail if x > pivot]
        return short_quick_sort(front) + [pivot] + short_quick_sort(rear)
    else:
        front = [x for x in tail if x >= pivot]
        rear = [x for x in tail if x < pivot]
        return short_quick_sort(front, True) + [pivot] + short_quick_sort(rear, True)






nums = [5,7,9,0,3,1,6,2,4,8]
#quick_sort(nums, 0, len(nums)-1)

print(short_quick_sort(nums, True))