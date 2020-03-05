#!/bin/python3

#Without using bisect you'll need to implement binary search on your own. Without binary search it won't be 
#possible to reduce the complexity of the problem. 
#The complexity of the current program is O(n)log(n+m)

import os
import sys

from bisect import bisect_left, bisect_right

# Complete the solve function below.
def solve(shots, players):
    low_list = []
    high_list = []
    count = sum = 0
    for index in range(0,len(shots)):
        low_list.append(shots[index][0])
        high_list.append(shots[index][1])
    low_list.sort()
    high_list.sort()
    for p in range(len(players)):
        leftmost = bisect_left(high_list, players[p][0])
        rightmost = bisect_right(low_list, players[p][1])
        count = rightmost - leftmost
        sum += count
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    shots = []

    for _ in range(n):
        shots.append(list(map(int, input().rstrip().split())))

    players = []

    for _ in range(m):
        players.append(list(map(int, input().rstrip().split())))

    result = solve(shots, players)

    fptr.write(str(result) + '\n')

    fptr.close()
