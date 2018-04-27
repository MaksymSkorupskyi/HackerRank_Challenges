"""List Comprehensions

https://www.hackerrank.com/challenges/list-comprehensions/problem

You are given three integers  and  representing the dimensions of a cuboid along with an integer .
You have to print a list of all possible coordinates given by  on a 3D grid where the sum of is not equal to .
 Here,

Input Format
Four integers  and  each on four separate lines, respectively.

Print the list in lexicographic increasing order.

Sample Input 0
1
1
1
2

Sample Output 0
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""

# x = y = z = 2
# n = 2

x, y, z, n = [int(input()) for i in range(4)]
print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (( i + j + k) != n)])