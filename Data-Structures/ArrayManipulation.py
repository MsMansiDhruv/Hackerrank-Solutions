#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.

#Code modified for O(n)
def arrayManipulation(n, queries):
    arr = [0]*(n+1)

    for x, y, incr in queries:
        arr[x-1] += incr
        if y <= len(arr):
            arr[y] -= incr
    m=x=0

    for i in arr:
        x += i
        if m < x:
            m = x
    return m

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
