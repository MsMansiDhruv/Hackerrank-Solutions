#!/bin/python3

import os
import sys

#
# Complete the twoStacks function below.
#   
def twoStacks(x, arr, brr):
    #
    # Write your code here.
    #
    i = j = tot = cnt = 0
    
    #Take required elements from arr A
    while i < len(arr) and ( tot + arr[i] ) <= x:
        tot += arr[i]
        i += 1
        cnt += 1     
    #tot = 10, i=3, cnt = 3"""
    
    #Take the elements of arr B and keep removing a to satisfy the condition
    while j < len(brr) and i >= 0:
        tot += brr[j]
        j += 1
        #tot = 12, j = 1
        #tot = 9, j = 2
        while i > 0 and tot > x:
            i -= 1
            tot -= arr[i]
            #i = 2, tot = 8
            #Not executed
        if cnt < (i+j) and tot <= x:
            cnt = (i+j)
            #Not executed
            #cnt = 4
    return cnt
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
