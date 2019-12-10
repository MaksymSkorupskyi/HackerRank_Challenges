"""Day 23: BST Level-Order Traversal

https://www.hackerrank.com/challenges/30-binary-trees/problem

A level-order traversal, also known as a breadth-first search, visits each level of a tree's nodes
from left to right, top to bottom.
You are given a pointer, root, pointing to the root of a binary search tree.
Complete the levelOrder function provided in your editor so that it prints the level-order traversal
of the binary search tree.

Hint: You'll find a queue helpful in completing this challenge.
"""


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if not root:
            return Node(data)
        if data <= root.data:
            cur = self.insert(root.left, data)
            root.left = cur
        else:
            cur = self.insert(root.right, data)
            root.right = cur
        return root

    # Level-Order Traversal (BFS)
    # A level-order traversal of tree is a recursive algorithm that processes the root,
    # followed by the children of the root (from left to right),
    # followed by the grandchildren of the root (from left to right), etc.
    def levelOrder(self, root):
        if not root:
            return None
        res = []
        nodes = [root]  # enqueue current root
        while nodes:  # while there are nodes to process
            next_nodes = []
            for node in nodes:
                res.append(node.data)
                # enqueue child elements from next level in order
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            nodes = next_nodes
        print(*res)


T = 6
arr = [3, 5, 4, 7, 2, 1]
myTree = Solution()
root = None
for i in range(T):
    # data = int(input())
    # root = myTree.insert(root, data)
    root = myTree.insert(root, arr[i])
myTree.levelOrder(root)
