"""Day 1: Interquartile Range
https://www.hackerrank.com/challenges/s10-interquartile-range/problem

The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles
(i.e., Q3-Q1).

Given an array, X, of n integers and an array, F, representing the respective frequencies of X's elements,
construct a data set, S, where each x occurs at frequency .
Then calculate and print S's interquartile range, rounded to a scale of  decimal place (i.e.,  format).

Tip: Be careful to not use integer division when averaging the middle two elements for a data set
with an even number of elements, and be sure to not include the median in your upper and lower data sets.

Input Format

The first line contains an integer, , denoting the number of elements in arrays  and .
The second line contains  space-separated integers describing the respective elements of array .
The third line contains  space-separated integers describing the respective elements of array .

Output Format

Print the interquartile range for the expanded data set on a new line.
Round your answer to a scale of  decimal place (i.e.,  format).

Sample Input
6
6 12 8 10 20 16
5 4 3 2 1 5

Sample Output
9.0
"""

x = [6, 12, 8, 10, 20, 16]
f = [5, 4, 3, 2, 1, 5]

def median(x):
    if len(x) % 2:
        return x[len(x) // 2]
    else:
        return (x[(len(x) // 2) - 1] + x[len(x) // 2]) / 2

n = input()
x = list(map(int, input().split()))
f = list(map(int, input().split()))
s = []
for i in range(len(x)):
    s += [x[i]] * f[i]
s.sort()
Q1 = median(s[:len(s) // 2])
Q3 = median(s[-(len(s) // 2):])
print(round(float(Q3-Q1), 1))

print("%.1f" % round(Q3 - Q1, 1)) # represent it with only one digit !!!



print(Q1, Q3, Q3-Q1, x, f, len(s), s, sep='\n')


"""
https://github.com/python/cpython/blob/3.6/Lib/statistics.py

def median(data):
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise StatisticsError("no median for empty data")
    if n%2 == 1:
        return data[n//2]
    else:
        i = n//2
        return (data[i - 1] + data[i])/2
"""