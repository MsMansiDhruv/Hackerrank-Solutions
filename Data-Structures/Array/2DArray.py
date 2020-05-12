#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    n = 6 
    sum = [[0]*n]*n
    
    #Maximum variable will have -63 as value because the minimum hour glass value possible is -9*7 = -63.
    max = -63
    
    #We take (n-2) here since we only want row, column to go till second last value; row+1, row+2 and col+1, col+2 will be added in the formula.
    for row in range(n-2):
        for col in range(n-2):
            sum[row][col] = arr[row][col] + arr[row][col+1] + arr[row][col+2] + arr[row+1][col+1] + arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
    
            if max < sum[row][col]:
                max = sum[row][col]
    return max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
