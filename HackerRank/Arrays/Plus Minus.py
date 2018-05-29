"""Plus Minus

https://www.hackerrank.com/challenges/plus-minus/problem

Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros.
Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places,
though answers with absolute error of up to  are acceptable.

Input Format

The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers describing an array of numbers .

Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size.
Sample Input

6
-4 3 -9 0 4 1
Sample Output

0.500000
0.333333
0.166667
"""

def plusMinus(arr):
    positive = negative = zeros = 0
    for i in arr:
        if i == 0:
            zeros += 1
        elif i < 0:
            negative += 1
        else:
            positive += 1
    print(round(positive/len(arr), 6))
    print(round(negative/len(arr), 6))
    print(round(zeros/len(arr), 6))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)