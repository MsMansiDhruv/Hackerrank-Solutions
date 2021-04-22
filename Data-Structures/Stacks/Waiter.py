#!/bin/python3

import os
import sys
from collections import deque
#
# Complete the waiter function below.
#
def generate_prime(lower, upper):
    prime_list = []
    for num in range(lower,upper + 1):  
        if num > 1:  
            for i in range(2,num):  
                if (num % i) == 0:  
                    break  
            else:  
                prime_list.append(num)  
    return prime_list

def waiter(number, q):
    pList = generate_prime(2, 10000)
    A = number.copy()
    B = []
    temp = []
    answers = []
    for i in range(0, q+1):
        B = []
        temp = []
        prime_number = pList.pop(0)
        while len(A) > 0:
            number = A.pop(0)
            if number%prime_number == 0:
                B.append(number)
            else:
                temp.append(number)
        answers += B
        temp.reverse()
        A = temp.copy()
    answers += A    
    return answers    
        
            
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
