#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c, m, dp):
    if n == 0:
        dp[n][m] = 1
        return dp[n][m]
    
    if n < 0:
        return 0
    
    if m < 0:
        return 0
    
    if dp[n][m] != -1:
        return dp[n][m]
    
    dp[n][m] = getWays(n - c[m], c, m, dp) + getWays(n, c, m - 1, dp)
    return dp[n][m]
    
    
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    dp = [[ -1 for _ in range(m)] for _ in range(n + 1)]
    ways = getWays(n, c, m - 1, dp)
    
    print(ways)

    # fptr.write(str(ways) + '\n')

    # fptr.close()
