import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    #Method 1: Pythonic hack. Complexity: O[k] k belongs to slice size for n input.
    """
    test_list = a[d:] + a[:d]  
    print(*test_list)  
    """
    
    #Method 2: Standard algorithm using two for loops. Complexity: O(n)^2
    #Time limit exceeded
    """
    temp = None
    for i in range(d):
        temp = a[0]
        for element in range(0,len(a)-1):
            # print(element)
            a[element] = a[element+1]
        a[element] = a[element+1]
        a[element+1] = temp
        # print(*a)
    
    print(*a)
    
    """
    
    #Method 3: Using stack technique using single for loop. Complexity: O(n)
    for i in range(d):
        top = a[0]
        a.remove(top)
        a.append(top)
    print(*a)
