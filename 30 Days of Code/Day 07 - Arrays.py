"""Day 7: Arrays

https://www.hackerrank.com/challenges/30-arrays/problem

Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

Sample Input
4
1 4 3 2

Sample Output
2 3 4 1
"""

input()
print(*input().split()[::-1])

# input()
# a = list(map(int, input().split()))
# print(*reversed(a))

"""
reversedarr = ''
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for i in range(n-1, -1, -1):
    reversedarr = reversedarr + str(arr[i]) + ' '

print(reversedarr)
"""
