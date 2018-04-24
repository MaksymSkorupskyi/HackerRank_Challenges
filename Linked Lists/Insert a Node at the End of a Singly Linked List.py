"""Linked List - insert new node at the end

Write a function to insert a node at the end of a Singly Linked-List.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next
    def insert(self, head, data):
        if not head: # null - initial list is empty
            head = Node(data) # create a first node
        else:
            cur_node = head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = Node(data) # create a new node
        return head


mylist = Solution()
T = 4  # int(input())
testcase = [2, 3, 4, 1]

head = None

for i in range(T):
    # data = int(input())
    # head = mylist.insert(head, data)
    head = mylist.insert(head, testcase[i])
    mylist.display(head)
    print()

# mylist.display(head)
