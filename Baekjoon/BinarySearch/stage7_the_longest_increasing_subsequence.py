from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
LIS_lenArray = [array[0]]

for num in array:
    
    if LIS_lenArray[-1] < num:
        LIS_lenArray.append(num)
    else:
        idx = bisect_left(LIS_lenArray,num)
        LIS_lenArray[idx] = num



print(len(LIS_lenArray))



