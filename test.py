#!/bin/python3

import math
import os
import random
import re
import ssl
import sys

#
# Complete the 'minesweeper' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER N
#  2. STRING_ARRAY bom
#

def minesweeper(N, bom):
    field = [ [0] * 10 for _ in range(10)]
    
    for i in range(N):
        curr_bom = bom[i]
        x, y = curr_bom.split(",")
        x = int(x) - 1
        y = int(y) - 1
        
        # set bom in field
        field[x][y] = -1 
        
        # set number around bom
        if x - 1 >= 0 and field[x - 1][y] != -1:
            field[x - 1][y] = field[x - 1][y] + 1
        if x + 1 < 10 and field[x + 1][y] != -1:
            field[x + 1][y] = field[x + 1][y] + 1
        if y - 1 >= 0 and field[x][y - 1] != -1:
            field[x][y - 1] = field[x][y - 1] + 1
        if y + 1 < 10 and field[x][y + 1] != -1:
            field[x][y + 1] = field[x][y + 1] + 1
            
        # diagonal l to r
        if x - 1 >= 0 and y - 1 >= 0 and field[x - 1][y - 1] != -1:
            field[x - 1][y - 1] = field[x - 1][y - 1] + 1
        if x + 1 < 10 and y + 1 < 10 and field[x + 1][y + 1] != -1:
            field[x + 1][y + 1] = field[x + 1][y + 1] + 1
        
        # diagonal r to l
        if y + 1 < 10 and x - 1 >= 0 and field[x - 1][y + 1] != -1:
            field[x - 1][y + 1] = field[x - 1][y + 1] + 1
        if y - 1 >= 0 and x + 1 < 10 and field[x + 1][y - 1] != -1:
            field[x + 1][y - 1] = field[x + 1][y - 1] + 1
    
    # build field
    res = []
    for i in range(10):
        curr_row = field[i]
        row_string = ""
        
        for j in curr_row:
            if j == -1:
                row_string = row_string + "X"
            elif j == 0:
                row_string = row_string + "."
            else:
                row_string = row_string + str(j)

        res.append(row_string)
    
    return res
        
        

if __name__ == '__main__':

    N = int(input().strip())

    bom = []

    for _ in range(N):
        bom_item = input()
        bom.append(bom_item)

    result = minesweeper(N, bom)

    print(result)
