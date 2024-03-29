class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)
    def insert(self, val):
        #Add your code here
        if self.root is None:
            self.root = Node(val)
            return
        
        #If tree is not null
        curr_node = self.root
        while val:
            if val > curr_node.info:
                if curr_node.right:
                    curr_node = curr_node.right
                else:
                    curr_node.right = Node(val)
                    break
            else:
                if curr_node.left:
                    curr_node = curr_node.left
                else:
                    curr_node.left = Node(val)
                    break
                    
        
tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
