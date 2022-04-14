import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))
maxNum = -1e9
minNum = 1e9

def backtraking(num, idx):
    global maxNum
    global minNum

    if idx == len(nums):
        if num > maxNum:
            maxNum = num
        if num < minNum:
            minNum = num
        return

    for i in range(4):
        if opers[i] == 0:
            continue

        opers[i] -= 1

        if i == 0:
            backtraking(num + nums[idx], idx+1)
        elif i ==1:
            backtraking(num - nums[idx], idx+1)
        elif i ==2:
            backtraking(num * nums[idx], idx+1)
        elif i ==3:
            if num < 0:
                backtraking(-(-num // nums[idx]), idx+1)
            else:
                backtraking(num // nums[idx], idx+1)
        opers[i] += 1

backtraking(nums[0], 1)        
print(maxNum)
print(minNum)

