#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'removeDuplicates' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

"""Algorithm 1: Creating new List """
# def removeDuplicates(llist):  
#     curr = llist
#     newList = SinglyLinkedListNode(0)
#     head = newList
#     # Write your code here
#     while(curr):
#         if not curr.next:
#             newList.next = None
#         if curr.data == newList.data:
#             curr = curr.next
#         else:
#             newList.next = curr
#             curr = curr.next
#             newList = newList.next
#     return head.next

"""Algorithm 2: Using the same list """
def removeDuplicates(llist):
    curr = llist
    while(curr.next):
        if(curr.data == curr.next.data):
            curr.next = curr.next.next
        else:
            curr = curr.next
    return llist    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = removeDuplicates(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
