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

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

"""Algorithm 1: Time Complexity O(n), Space Complexity O(n)"""
# def has_cycle(head):
#     curr = head
#     nodes = set()
#     isCircular = False
#     while(curr):
#         if curr in nodes:
#             return True
#         else:
#             nodes.add(curr)
#         curr = curr.next
#     return False

"""
Algorithm 2: Floyd's Cycle Finding Algorithm, Time Complexity O(n), Space Complexity O(1)
This algorithm makes use of two pointers, one which moves one step at a time and another which moves two step at a time. The idea is if there is a cycle, the two pointers will meet at one specific node else they never meet. 
"""
def has_cycle(head):
    slow = head
    fast = head
    while(slow and fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1);
        temp = llist.head;

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count-1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()
