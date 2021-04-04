#!/bin/python3

import os
import sys
from collections import deque
#
# Complete the andXorOr function below.
#
def andXorOr(a):
    #
    # Write your code here.
    #
    #Initialise max_sum, stack
    #Add first element to stack
    #Traverse loop
        #While stack is not empty
            #Get top
            #Calculate res=curr_element^top
            #If res > max_sum, assign result to max_sum
            #If curr_element < top, pop the element from stack, else break
        #Push curr_element to stack 
    #Return max_sum
    stack = deque()
    stack.append(a[0])
    max_sum = a[0]^a[1]
    for i in range(1, len(a)):
        while len(stack) > 0:
            top = stack[-1]
            exp = a[i]^top
            if exp > max_sum:
                max_sum = exp
            if a[i] < top:
                stack.pop()
            else:
                break
        stack.append(a[i])
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    fptr.write(str(result) + '\n')

    fptr.close()
