#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    substrings = {}
    # find all substring
    # then sort and add to hash
    
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            subs = s[i:j]
            sorted_subs = ''.join(sorted(subs))
            
            
            try:
                substrings[sorted_subs] += 1 
            except:
                substrings[sorted_subs] = 1
    
    count_anagram = 0
    
    for k in substrings.keys():
        if substrings[k] > 1:
            # combination
            count_anagram += substrings[k] * (substrings[k] - 1) / 2
        
    return int(count_anagram)
            

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)

    # fptr.close()
