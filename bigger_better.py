#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    not_ascended_idx = len(w) - 2
    
    # find not sorted
    while not_ascended_idx >= 0 and w[not_ascended_idx] >= w[not_ascended_idx + 1]:
        not_ascended_idx -= 1
    
    # return no answer if already sorted
    if not_ascended_idx < 0:
        return 'no answer'

    # find smallest greatest, then swap
    for j in range(len(w) - 1, not_ascended_idx, -1):
        if w[not_ascended_idx] < w[j]:
            # swap character
            w = w[:not_ascended_idx] + w[j] + w[not_ascended_idx+1:j] + w[not_ascended_idx] + w[j+1:]
            
            # reverse substring to the right of not_ascended_idx to find smallest lexicograph order
            # substring to the right is already sorted biggest -> smallest (left to right)
            s = w[:not_ascended_idx+1]
            y = w[:not_ascended_idx:-1]
            w = s + y
            break
        
    
    return w

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)
    #     fptr.write(result + '\n')

    # fptr.close()
