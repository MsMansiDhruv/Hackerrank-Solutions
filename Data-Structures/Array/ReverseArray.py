#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    #Method 1: Reverse array by taking another array
    # j = len(a)
    # b = [None] * len(a)
    # for i in range( 0, len(a) ):
    #     b[j-1] = a[i]
    #     j = j-1
    #     print(j)
    # return b

    #Method 2: Reverse array by swapping elements
    j = len(a)
    # b = [None] * j
    for i in range(int(j/2)):
        temp = a[i]
        a[i] = a[j-i-1]
        a[j-i-1] = temp
    return a
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
