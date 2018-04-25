"""Day 22: Binary Search Trees - height

https://www.hackerrank.com/challenges/30-binary-search-trees/problem

The height of a binary search tree is the number of edges between the tree's root and its furthest leaf.
You are given a pointer, root, pointing to the root of a binary search tree.
Complete the getHeight function provided in your editor so that it returns the height of the binary search tree.
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
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

    def getHeight(self, root):
        if not root:
            return -1
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def getHeight(self, root):
        if root is None:
            return 0
        lheight = self.getHeight(root.left)
        rheight = self.getHeight(root.right)
        if lheight > rheight:
            if root.left:
                return lheight + 1
            return lheight
        else:
            if root.right:
                return rheight + 1
            return rheight

T = 7
arr = [3, 5, 2, 1, 4, 6, 7]
myTree = Solution()
root = None
for i in range(T):
    # data = int(input())
    root = myTree.insert(root, arr[i])
print(root, root.data)
height = myTree.getHeight(root)
print(height)
