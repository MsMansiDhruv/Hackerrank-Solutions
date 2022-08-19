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

    #Pythonic hack
    """
    test_list = a[d:] + a[:d]  
    print(*test_list)  
    """
    
    #Standard algorithm 
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
    
    #Using stack technique
    for i in range(d):
        top = a[0]
        a.remove(top)
        a.append(top)
    print(*a)
