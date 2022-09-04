#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

"""Taking 3 different stacks. Time complexity: O(n), Space complexity: O(n)"""
def getMax(operations):
    stck = []
    result = []
    mx = []
    rows = []
    # Write your code here
    for rowVal in operations:
        rows = rowVal.split(" ")
        if rows[0] == "1":
            val = int(rows[1])
            stck.append(val)
            if not mx or val >= mx[-1]: mx.append(val)
        elif rows[0] == "2":
            if stck: 
                ele = stck.pop()
            if mx and ele == mx[-1]:
                mx.pop()
        else:
            result.append(mx[-1])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
