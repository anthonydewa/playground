#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pylons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pylons(k, arr):
    n = len(arr)
    count = 0
    i = 0
    
    while i < n:
        found = False
        
        starting_point = min(n - 1, i + k - 1)
        endpoint = max(-1, i - k)
        
        for j in range(starting_point, endpoint, -1):
            if arr[j] == 1:
                i = j + k
                found = True
                count += 1
                break
        
        if not found:
            return -1
    
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)

    print(result)

    # fptr.close()
