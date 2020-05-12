
# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    if head.next is None:
        print(head.data)
        return None
    print(head.data)
    printLinkedList(head.next)
if __name__ == '__main__':
