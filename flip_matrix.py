#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    result = 0
    matrix_length = len(matrix)
    matrix_max_idx = matrix_length - 1
    for i in range(matrix_length // 2):
        for j in range(matrix_length // 2):
            biggest_curr_upper_left_quadran = matrix[i][j]
            
            ## find three other corresponding value
            # 1
            v1 = matrix[i][matrix_max_idx - j]
            v2 = matrix[matrix_max_idx - i][j]
            v3 = matrix[matrix_max_idx - i][matrix_max_idx - j]
            
            result += max(biggest_curr_upper_left_quadran, v1, v2, v3)
            
    return result
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        print(result)

    # fptr.close()
