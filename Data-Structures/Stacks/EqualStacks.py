#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#
    
def equalStacks(h1, h2, h3):
    s1, s2, s3 = map(sum, (h1,h2,h3))
    print(s1, s2, s3)
    while h1 and h2 and h3:
        m = min(s1, s2, s3)
        while s1>m:
            element = h1.pop(0)
            s1 -= element
        while s2>m:
            element = h2.pop(0)
            s2 -= element
        while s3>m:
            element = h3.pop(0)
            s3 -= element
        if s1==s2==s3:
            return s1
    return 0
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
