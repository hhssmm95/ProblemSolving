#!/bin/python3

import math
import os
import random
import re
import sys
from turtle import right


def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    answer = 0
    
    up_line = abs(r_q-n)
    down_line = abs(r_q-1)
    left_line = abs(c_q-1)
    right_line = abs(c_q-n)
    LU_diagonal = min(abs(r_q-n), abs(c_q-1))
    RU_diagonal = min(abs(r_q-n), abs(c_q-n))
    LD_diagonal = min(abs(r_q-1), abs(c_q-1))
    RD_diagonal = min(abs(r_q-1), abs(c_q-n))

    for obs_r, obs_c in obstacles:
        r_diff, c_diff = (abs(r_q-obs_r), abs(c_q-obs_c))
        
        #diagonal
        if r_diff == c_diff:
            #down
            if r_q - obs_r > 0:
                if c_q - obs_c < 0:
                    RD_diagonal = min(RD_diagonal, r_diff-1)
                else:
                    LD_diagonal = min(LD_diagonal,r_diff-1)
            #up
            else:
                if c_q - obs_c < 0:
                    RU_diagonal = min(RU_diagonal,r_diff-1)
                else:
                    LU_diagonal = min(LU_diagonal, r_diff-1)
        #horizontal
        elif r_diff == 0:
            if c_q - obs_c < 0:
                right_line = min(right_line, c_diff-1)
            else:
                left_line = min(left_line, c_diff-1)
        #vertical
        elif c_diff == 0:
            if r_q - obs_r < 0:
                up_line = min(up_line, r_diff-1)
            else:
                down_line = min(down_line, r_diff-1)

    answer = up_line + down_line + right_line + left_line + LU_diagonal + RU_diagonal + LD_diagonal + RD_diagonal

    return answer

print(queensAttack(4,0,4,4,[]))