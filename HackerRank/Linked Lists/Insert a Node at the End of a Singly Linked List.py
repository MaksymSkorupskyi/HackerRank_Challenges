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

    def insert(self, head, data): # insert new node at the end
        if not head: # if initial list is empty
            return Node(data) # create a first node
        cur_node = head
        while cur_node.next: # seeking last node
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
