"""Day 1: Standard Deviation
https://www.hackerrank.com/challenges/s10-standard-deviation/problem

Given an array, X, of N integers, calculate and print the standard deviation.
Your answer should be in decimal form, rounded to a scale of  decimal place (i.e.,  format).
An error margin of  will be tolerated for the standard deviation.

Input Format

The first line contains an integer, , denoting the number of elements in the array.
The second line contains  space-separated integers describing the respective elements of the array.

Output Format

Print the standard deviation on a new line, rounded to a scale of  decimal place (i.e.,  format).

Sample Input
5
10 40 30 50 20

Sample Output
14.1
"""

x = [10, 40, 30, 50, 20]

# n = input()
# x = list(map(int, input().split()))
mean = sum(x)/len(x)
variance = sum((i - mean) ** 2 for i in x) / len(x)
standard_deviation = variance ** 0.5
print(round(standard_deviation, 1))


print(standard_deviation, mean, variance, x, sep='\n')