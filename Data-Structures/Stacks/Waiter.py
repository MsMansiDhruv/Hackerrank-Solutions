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

def waiter(numbers, q):
    pList = generate_prime(2, 10000)
    A = []
    B = []
    temp = []
    answers = []
    
    prime_number = pList.pop(0)
    while len(numbers) > 0:
        number = numbers.pop(0)
        if number%prime_number == 0:
            answers.append(number)
        else:
            temp.append(number)
    
    A = temp.copy()         
    for i in range(1, q):
        B = []
        temp = []
        prime_number = pList.pop(0)
        while len(A) > 0:
            number = A.pop()
            if number%prime_number == 0:
                answers.append(number)
            else:
                temp.append(number)
        A = temp.copy()
    for val in A:
        answers.append(val)  
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
