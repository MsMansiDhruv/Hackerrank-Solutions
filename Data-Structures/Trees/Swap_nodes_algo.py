#!/bin/python3

import os
import sys
from queue import Queue
#
# Complete the swapNodes function below.
#
class Node:
    def __init__(self, val, level):
        self.info = val
        self.level = level
        self.left = None
        self.right = None

def inorder(root, item):
    if root:
        inorder(root.left, item)
        item.append(root.info)
        inorder(root.right, item)

def createTree(indexes):
    #using queue to create the tree: BFS
    q = Queue()
    root = Node(1, 1)
    maxlevel = 1
    q.put(root)
    for left, right in indexes:
        cur = q.get()
        if left != -1:
            leftNode = Node(left, cur.level + 1)
            cur.left = leftNode
            q.put(leftNode)
        if right != -1:
            rightNode = Node(right, cur.level + 1)
            cur.right = rightNode
            q.put(rightNode)
        #Finally the q is empty, and cur is at lowest level. Because there are always [-1, -1]s at the end of the indexes
        maxlevel = cur.level
    return (root, maxlevel)
    
def swap(root, k):
    if root.left:
        swap(root.left, k)
    if root.right:
        swap(root.right, k)
    if root.level in k:
        root.left, root.right = root.right, root.left
    return root
    
def swapNodes(indexes, queries):
    #
    # Write your code here.
    #
    #Create tree
    sys.setrecursionlimit(1500)
    root, maxLevel = createTree(indexes)
    ret = []
    #Swap nodes
    for k in queries:
        item = []
        h = [x for x in range(1, maxLevel) if x%k == 0]
        root = swap(root, h)   
        inorder(root, item)
        ret.append(item)
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)
    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    # fptr.write(str(result))
    fptr.write('\n')

    fptr.close()
