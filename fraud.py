#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    n = len(expenditure)
    notified = 0
    sorted_prev = sorted(expenditure[:d])
    median_prev_idx = (d // 2)

    for i in range(d, n):
        curr_expend = expenditure[i]

        if d % 2 == 0:
            median = (sorted_prev[median_prev_idx - 1] + sorted_prev[median_prev_idx]) / 2
        else:
            median = sorted_prev[median_prev_idx]
        # add notified
        if curr_expend >= median * 2:
            notified += 1
        
        # new sorted
        # TODO improve sort
        prev_sorted_update(sorted_prev, expenditure[i - d], curr_expend, d)
        
    return notified

def prev_sorted_update(list, to_be_deleted, to_be_inserted, d):
    # del 
    del_low = 0
    del_high = d - 1
    while del_low <= del_high:
        m = del_low + (del_high - del_low) // 2
        if list[m] == to_be_deleted:
            list.pop(m)
            break
        
        elif list[m] < to_be_deleted:
            del_low = m + 1
        else:
            del_high = m - 1
        
    # insert
    ins_low = 0
    ins_high = d - 2
    while ins_low <= ins_high: 
        m = ins_low + (ins_high - ins_low) // 2
        
        if list[m] <= to_be_inserted and m+1 > d - 2:
            list.insert(m + 1, to_be_inserted)
            break
        elif list[m] >= to_be_inserted and m-1 < 0:
            list.insert(m, to_be_inserted)
            break
        elif list[m] <= to_be_inserted and to_be_inserted <= list[m+1]:
            list.insert(m + 1, to_be_inserted)
            break
        elif list[m - 1] <= to_be_inserted and to_be_inserted <= list[m]:
            list.insert(m, to_be_inserted)
            break
        
        elif list[m] < to_be_inserted:
            ins_low = m + 1
        else:
            ins_high = m - 1

    return list 
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(result)

    # fptr.close()
