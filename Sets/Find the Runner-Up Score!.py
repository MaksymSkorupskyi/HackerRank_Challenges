"""Find the Runner-Up Score!

https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given scores. Store them in a list and find the score of the runner-up.

Sample Input 0
5
2 3 6 6 5

Sample Output 0
5
"""

n = int(input())
arr = map(int, input().split())

print(sorted(set(arr))[-2])