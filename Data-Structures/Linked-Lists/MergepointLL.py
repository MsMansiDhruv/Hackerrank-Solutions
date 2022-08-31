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

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

"Time complexity: O(mn) where m and n are number of nodes in head1 and head2"
# def findMergeNode(head1, head2):
#     while(head2):
#         temp = head1
#         while(temp):
#             if temp == head2:
#                 return head2.data
#             temp=temp.next
#         head2 = head2.next
#     return None

"""Time Complexity: O(n) where n is number of nodes in head1 or head2"""
def findMergeNode(head1, head2):
    h1 = head1
    s1 = 0
    s2 = 0
    h2 = head2
    #Get size of list
    while(h1):
        s1 += 1
        h1 = h1.next
    while(h2):
        s2+=1 
        h2=h2.next
        
    h1 = head1
    h2 = head2
    
    #Calculate distance of the bigger linked list and iterate over it till we make the number of nodes same.
    if s1>s2: 
        d=s1-s2
        for i in range(d):
            h1 = h1.next
    else: 
        d=s2-s1
        for i in range(d):
            h2 = h2.next
            
    #Now both the linked list have same number of nodes, we iterate over both and find the merging node
    while(h1 and h2):
        if h1 == h2:
            return h1.data
        h1 = h1.next
        h2 = h2.next
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)
            
        ptr1 = llist1.head;
        ptr2 = llist2.head;

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
                
        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()
