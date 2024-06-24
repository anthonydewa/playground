#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'xorAndSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def xorAndSum(a, b):
    new_a = int(a, 2)
    new_b = int(b, 2)
    mod = 10 ** 9 + 7
    i = 314160
    res = 0
    
    for j in range(i):
        res += new_a ^ (new_b << j)
    
    return res % mod

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    result = xorAndSum(a, b)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
