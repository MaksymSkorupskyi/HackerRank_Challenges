"""Day 0: Weighted Mean
https://www.hackerrank.com/challenges/s10-weighted-mean/problem

In the previous challenge, we calculated a mean. In this challenge, we practice calculating a weighted mean.

Task
Given an array, X, of N integers and an array, W, representing the respective weights of 's elements, calculate and print the weighted mean of 's elements. Your answer should be rounded to a scale of  decimal place (i.e.,  format).

Input Format:

The first line contains an integer, , denoting the number of elements in arrays  and .
The second line contains  space-separated integers describing the respective elements of array .
The third line contains  space-separated integers describing the respective elements of array .


Output Format:

Print the weighted mean on a new line.
Your answer should be rounded to a scale of  decimal place (i.e.,  format).

Sample Input
5
10 40 30 50 20
1 2 3 4 5

Sample Output:
32.0
"""

n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

weighted = 0
for i in range(len(x)):
    weighted += x[i] * w[i]

print(round(weighted/sum(w), 1))



#
N = map(int,input().split())
X = list(map(int, input().strip().split(' ')))
W = list(map(int, input().strip().split(' ')))
sum_X = sum([a*b for a,b in zip(X,W)])
print(round((sum_X/sum(W)),1))
