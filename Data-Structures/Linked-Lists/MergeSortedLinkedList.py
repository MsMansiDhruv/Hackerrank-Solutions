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

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#if head.next is None:
#
def mergeLists(head1, head2):
    head = SinglyLinkedListNode(0)
    ptr = head
        
    while True:
        if head1 is None and head2 is None:
            break
        elif head1 is None:
            ptr.next = head2
            break
        elif head2 is None:
            ptr.next = head1
            break
        else:
            smallestVal = 0
            if head1.data >= head2.data:
                smallestVal = int(head2.data)
                print(f"head1.data is {head1.data} ")
                print(f"head2.data is {head2.data} ")
                print(f"head2 is {smallestVal} ")
                head2 = head2.next
            else:
                smallestVal = head1.data
                print(f"head1.data is {head1.data} ")
                print(f"head2.data is {head2.data} ")
                print(f"head2 is {smallestVal} ")
                head1 = head1.next
                
            newNode = SinglyLinkedListNode(smallestVal)
            ptr.next = newNode
            ptr = ptr.next
            
    return head.next
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
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

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
