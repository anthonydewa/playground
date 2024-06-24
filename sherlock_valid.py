#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    freq_hash = {}
    
    len(s)
    
    for i in range(len(s)):
        char = s[i]
        
        try:
            freq_hash[char] += 1
        except KeyError:
            freq_hash[char] = 1

    if len(freq_hash) == 1:
        return 'YES'
    
    lst = list(freq_hash.values())
    if len(lst) == 2:
        if abs(lst[0] - lst[1]) > 1:
            return 'NO'
        else:
            return 'YES'

    common_freq = -1
    common_freq_count = 0
    least_freq = -1
    least_freq_count = 0
    for i in range(len(lst)):
        curr_freq = lst[i]
        
        if common_freq == -1:
            common_freq = curr_freq
            common_freq_count += 1
        elif curr_freq == common_freq:
            common_freq_count += 1
        elif curr_freq != common_freq and least_freq == -1:
            least_freq = curr_freq
            least_freq_count += 1
        elif curr_freq == least_freq:
            least_freq_count += 1
        elif curr_freq != common_freq and curr_freq != least_freq:
            return 'NO'
        
        if common_freq_count <= least_freq_count:
            common_freq, least_freq = least_freq, common_freq
            common_freq_count, least_freq_count = least_freq_count, common_freq_count
    
    if abs(common_freq - least_freq) <= 1 and least_freq_count <= 1 or least_freq == -1 or least_freq <= 1 and least_freq_count <= 1:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    f = open('f.txt', 'r')
    s = f.read().rstrip()
    
    print('y')

    result = isValid(s)

    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
