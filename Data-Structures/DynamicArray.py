#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    last_answer = length = index = 0
    int_array = []
    seqList = [[] * (n-1) for i in range(n)]
    for loop in range(0, len(queries)):
        index = (int(queries[loop][1]) ^ int(last_answer)) % n
        if queries[loop][0] == 1:
            seqList[index].append(queries[loop][2])
        elif queries[loop][0] == 2:
            length = len(seqList[index])
            index2 = queries[loop][2] % length
            last_answer = seqList[index][index2]
            int_array.append(last_answer)
    return int_array

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
