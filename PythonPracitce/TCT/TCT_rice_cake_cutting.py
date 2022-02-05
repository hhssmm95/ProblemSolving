
def binary(start, end, target, heights):
    if start > end:
        return None

    mid = (start + end) // 2

    gain = 0
    for i in heights:
        if i > mid:
            gain += i - mid
    
    if gain == target:
        return mid

    elif gain < target:
        return binary(start, mid-1, target, heights)
    elif gain > target:
        return binary(mid+1, end, target, heights)

def solution(heights, m):



    heights.sort()

    h = heights[len(heights)-1]

    answer = binary(0, h, m, heights)
    return answer




print(solution([19, 15, 10, 17], 6))
