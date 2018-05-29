"""Day 1: Quartiles
https://www.hackerrank.com/challenges/s10-quartiles/problem

Task
Given an array, X, of n integers,
calculate the respective first quartile (), second quartile (), and third quartile ().
It is guaranteed that Q1, Q2, and Q3
 are integers.

Input Format
The first line contains an integer, , denoting the number of elements in the array.
The second line contains  space-separated integers describing the array's elements.

Output Format
Print  lines of output in the following order:

The first line should be the value of Q1.
The second line should be the value of Q2.
The third line should be the value of Q3.

Sample Input
9
3 7 8 5 12 14 21 13 18

Sample Output
6
12
16
"""


x = [1, 3, 5, 7, 8, 12, 13, 14, 18, 21]

def median(x):
    if len(x) % 2:
        return x[len(x) // 2]
    else:
        return (x[len(x) // 2 - 1] + x[len(x) // 2]) / 2

# n = input()
# x = sorted(map(int, input().split()))
Q1 = median(x[:len(x) // 2])
Q2 = median(x)
Q3 = median(x[-(len(x) // 2):])
print(int(Q1), int(Q2), int(Q3), sep='\n')

print(int(median(x[:len(x) // 2])), int(median(x)), int(median(x[- (len(x) // 2):])), sep='\n')



print(x[:len(x) // 2])
print(x[- (len(x) // 2):])
print(len(x), len(x) // 2, x, int(median(x[:len(x) // 2])), int(median(x)), int(median(x[len(x) // 2:])), sep='\n')

