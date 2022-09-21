#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the largestRectangle function below.

#Time Complexity: O(n), Space Complexity: O(n)
def previousSmaller(h):
    indexI = []
    indexJ = []
    val = []
    for i in range(0,len(h)):
        while(len(val)>0 and val[-1]>=h[i]):
            val.pop()
            indexJ.pop()

        if len(val)==0:
            indexI.append(-1)
        else:
            indexI.append(indexJ[-1])
        indexJ.append(i)
        val.append(h[i])  
    return indexI
    
def nextSmaller(h):
    indexI = []
    indexJ = []
    val = []
    n = len(h)
    for i in range(n-1, -1, -1):
        while(len(val)>0 and val[-1]>=h[i]):
            val.pop(-1)
            indexJ.pop(-1)
        if len(val)==0:
            indexI.append(n)
        else:
            indexI.append(indexJ[-1])
        indexJ.append(i)
        val.append(h[i])
    return indexI[::-1]        
    
def largestRectangle(h):
    l = previousSmaller(h)
    m = nextSmaller(h)
    area = [e2-e1-1 for e1,e2 in zip(l,m) ]
    for i in range(len(h)):
        area[i] = area[i]*h[i]
    return max(area)
    
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
