#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words
#

def crosswordPuzzle(crossword, words):
    # locate all empty
    sss = []
    for i in range(10):
        for j in range(10):
            char = crossword[i][j]
            
            if char == '-':
                # check up & left if exist - char
                # if exist, then is it part of existing sequence
                # if not, then is it new sequence
                
                
                
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crossword = []

    for _ in range(10):
        crossword_item = input()
        crossword.append(crossword_item)

    words = input()

    result = crosswordPuzzle(crossword, words)

    print('\n'.join(result))
    print()
