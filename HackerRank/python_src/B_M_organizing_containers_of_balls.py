#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    n = len(container)
    #서로 다른 컬러 공의 합 list
    type_sums = [0] * n
    #서로 다른 컨테이너의 공간 합 list
    container_sums = [sum(li) for li in container]
    
    for c in range(n):
        for r in range(n):
            type_sums[c]+=container[r][c]

    #정렬 (한 색의 공을 한 컨테이너에 몰아넣은것과 같음)
    type_sums.sort()
    container_sums.sort()

    #정렬된 공의 개수가 컨테이너 공간과 맞지 않으면 불가능
    for i in range(n):
        if type_sums[i] != container_sums[i]:
            return "Impossible"            

    return "Possible"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
