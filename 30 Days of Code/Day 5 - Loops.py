"""Day 5: Loops

https://www.hackerrank.com/challenges/30-loops/problem
Given an integer, n, print its first 10 multiples.

Sample Input
2

Sample Output
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
"""

n = int(input().strip())

for i in range(1, 11):
    print(n,'x', i, '=', n * i)