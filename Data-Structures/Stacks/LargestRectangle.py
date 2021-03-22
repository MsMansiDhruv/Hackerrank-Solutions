import math
import os
import random
import re
import sys
from collections import deque

# Complete the largestRectangle function below.
def largestRectangle(h):
    pos = deque()
    height = deque()
    max_area = 0
    iterator = 0
    
    while (iterator < len(h) ):
        if len(height)==0 or len(pos) == 0 or h[iterator] >= height[-1]:
            height.append(h[iterator])
            pos.append(iterator)
        elif len(height) > 0 and len(pos) > 0 and h[iterator] < height[-1]:
            while len(height) > 0 and len(pos) > 0 and h[iterator] < height[-1]: 
                element = height.pop()
                index = pos.pop()
                print(index)
                no_of_buildings = iterator - index
                area = element * no_of_buildings
                max_area = max(area, max_area)
                # print(height, pos)
            height.append(h[iterator])
            pos.append(index)
        iterator += 1
    while len(height) > 0:
        element = height.popleft()
        index = pos.popleft()
        area = (len(h) - index) * element
        max_area = max(area, max_area)    
    return max_area
                        
    
    
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
