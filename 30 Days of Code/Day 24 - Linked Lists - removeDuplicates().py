"""Day 24 - linked_lists - removeDuplicates()

https://www.hackerrank.com/challenges/30-linked-list-deletion/problem

A removeDuplicates function is declared in your editor,
which takes a pointer to the root node of a linked list as a parameter.
Complete removeDuplicates so that it deletes any duplicate nodes from the list
and returns the head of the updated list.

Note: The head pointer may be null, indicating that the list is empty.
Be sure to reset your next pointer when performing deletions to avoid breaking the list.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data): # insert new node at the end
        if not head: # if initial list is empty
            return Node(data) # create a first node
        cur_node = head
        while cur_node.next: # seeking last node
            cur_node = cur_node.next
        cur_node.next = Node(data) # create a new node
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        cur_node = head
        while cur_node.next:
            if cur_node.data == cur_node.next.data:
                cur_node.next = cur_node.next.next
            else:
                cur_node = cur_node.next
        return head

mylist = Solution()

# T = 6  # int(input())
# testcase = [1, 2, 2, 3, 3, 4]

T = 20
testcase = [3,9,9,11,11,11,11,89,89,
100,
100,
101,
102,
103,
108,
200,
250,
250,
250,
250]

head = None
for i in range(T):
    head = mylist.insert(head, testcase[i])
mylist.display(head)
head = mylist.removeDuplicates(head)
print('\n','remove duplicates:')
mylist.display(head)
