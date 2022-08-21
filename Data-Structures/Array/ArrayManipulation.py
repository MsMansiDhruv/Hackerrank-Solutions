#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.

#Code modified for O(n)
def arrayManipulation(n, queries):
    #Note: The indexing in example starts from 1. The a and b values are inclusive
    
    #Method 1: Brute force: Using 2+1 for loops. Complexity: O(n^q), q=length of queries, n=input
    """
    arr = [0]*n
    maxVal = 0
    for a,b,k in queries:
        for i in range(a-1,b):
            arr[i]+=int(k)
    for val in arr:
        if maxVal < val: maxVal = val
    return maxVal   
    """
    
    #Method 2: Using prefix Sum algorithm. Complexity: O(q) + O(n), q=length of queries, n=input 
    arr = [0]*(n+1) #Take one extra element for easy indexing.
    maxVal = 0
    x = 0
    for a,b,k in queries:
        arr[a-1] += k
        if b <= len(arr):
            arr[b] -= k
            
    for i in arr:
        x+=i
        if x>maxVal: maxVal=x
        
    return maxVal
        

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
