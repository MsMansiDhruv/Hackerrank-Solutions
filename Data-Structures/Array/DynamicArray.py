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
    arr = [[] * (n) for i in range(n)]
    lastAnswer = 0
    ans = []
    for a,x,y in queries:
        idx = ((int(x)^lastAnswer)%n)
        if int(a)==1:
            #Run query 1
            arr[idx].append(int(y))
            print(arr[idx])
        elif int(a)==2:
            #Run query 2
            lastAnswer = arr[idx][int(y)%len(arr[idx])]
            ans.append(lastAnswer)
    return ans

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
