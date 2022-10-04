#!/bin/python3

from itertools import permutations
import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

# 1. 수가 k로 나누어 떨어지는 경우 (부분집합 내에 하나만 포함 가능)
# 2. k가 짝수일때 나머지가 k/2인 경우 (부분집합 내에 하나만 포함 가능)
# 3. 두 수의 나머지 합이 k로 나누어 떨어지는 경우

def nonDivisibleSubset(k, s):
    remain_li = [0]*k
    answer = 0

    half = False

    for num in s:
        remain_li[num%k]+=1
        

    if remain_li[0] != 0:
        answer+=1

    if k%2 == 0 and remain_li[k//2] != 0:
        answer+=1
    


    for i in range(1,k//2+1):
        #k가 짝수일떄 나머지가 k/2인 경우는 이미 위에서 하나 뽑았음
        if k%2 == 0 and i == k//2:
            continue
        answer += max(remain_li[i], remain_li[k-i])
        
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
