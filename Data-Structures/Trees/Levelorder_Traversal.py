class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value 
of the node)
"""
from collections import OrderedDict 

def printLevelOrder(root, height, hd, m):
    if root == None:
        return
    
    if height not in m:
        m[height] = [root.info]
    else:
        m[height].append(root.info)
        
    printLevelOrder(root.left, height+1, hd-1, m)
    printLevelOrder(root.right, height+1, hd+1, m)
    

def levelOrder(root):
    #Write your code here
    m = OrderedDict()
    printLevelOrder(root, 0, 0, m)
    
    l=[]
    for i in m:
        l+= m[i]
    print(*l, sep = ' ')

