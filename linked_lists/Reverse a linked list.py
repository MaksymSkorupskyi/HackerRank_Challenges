"""Reverse a linked list

https://www.hackerrank.com/challenges/reverse-a-linked-list/problem

You’re given the pointer to the head node of a linked list.
Change the next pointers of the nodes so that their order is reversed.
The head pointer given may be null meaning that the initial list is empty.

Input Format
You have to complete the Node* Reverse(Node* head) method which takes one argument - the head of the linked list.
You should NOT read any input from stdin/console.

Output Format
Change the next pointers of the nodes that their order is reversed and return the head of the reversed linked list.
Do NOT print anything to stdout/console.

Sample Input
NULL
2 --> 3 --> NULL

Sample Output
NULL
3 --> 2 --> NULL

Explanation
1. Empty list remains empty
2. List is reversed from 2,3 to 3,2
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def Reverse(head):
        if not head:
            return head
        prev_node = None
        curr_node = head
        while curr_node:
            next_node = curr_node.next # Remember next node
            curr_node.next = prev_node # REVERSE! None, first time round.
            prev_node = curr_node  # Used in the next iteration.
            curr_node = next_node  # Move to next node.
        return prev_node