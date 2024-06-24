#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    vu = vd = hl= hr= dul= dur= ddl= ddr = True
    vu_val = vd_val = hl_val = hr_val = dul_val = dur_val = ddl_val = ddr_val = n
    
    
    for i in range(k):
        obs = obstacles[i]
        
        x = obs[0]
        y = obs[1]
        
        # vertical
        if x == r_q:
            if c_q < y:
                vu = False
                temp_vu_val = abs(y - c_q) - 1
                
                if temp_vu_val < vu_val:
                    vu_val = temp_vu_val
            else:
                vd = False
                temp_vd_val = abs(c_q - y) - 1
                
                if temp_vd_val < vd_val:
                    vd_val = temp_vd_val        
        
        # horizontal
        if y == c_q:
            if r_q < x:
                hr = False
                temp_hr_val = abs(x - r_q) - 1
                
                if temp_hr_val < hr_val:
                    hr_val = temp_hr_val
            else:
                hl = False
                temp_hl_val = abs(r_q - x) - 1
                
                if temp_hl_val < hl_val:
                    hl_val = temp_hl_val
        
        # diagonal
        if abs(x - r_q) == abs(y - c_q):
            if r_q < x and c_q < y:
                dur = False
                temp_dur_val = y - c_q - 1
                
                if temp_dur_val < dur_val:
                    dur_val = temp_dur_val
            elif r_q > x and c_q < y:
                dul = False
                temp_dul_val = y - c_q - 1
                
                if temp_dul_val < dul_val:
                    dul_val = temp_dul_val
            elif r_q < x and c_q > y:
                ddr = False
                temp_ddr_val = c_q - y - 1
                
                if temp_ddr_val < ddr_val:
                    ddr_val = temp_ddr_val
            elif r_q > x and c_q > y:
                ddl = False
                temp_ddl_val = c_q - y - 1
                
                if temp_ddl_val < ddl_val:
                    ddl_val = temp_ddl_val
    
    if vu:
        vu_val = n - c_q
    if vd:
        vd_val = c_q - 1
    if hr:
        hr_val = n - r_q
    if hl:
        hl_val = r_q - 1
    if dul:
        dul_val = min(n - c_q, r_q - 1)
    if dur:
        dur_val = min(n - c_q, n - r_q)
    if ddl:
        ddl_val = min(c_q - 1, r_q - 1)
    if ddr:
        ddr_val = min(c_q - 1, n - r_q)
        
    
    return vu_val + vd_val + hl_val + hr_val + dul_val + dur_val + ddl_val + ddr_val
        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)
    
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
