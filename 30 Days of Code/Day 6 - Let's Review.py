"""Day 6: Let's Review

https://www.hackerrank.com/challenges/30-review-loop/problem

Given a string, S, of length N that is indexed from 0 to N-1,
print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line
(see the Sample below for more detail).

Sample Input
2
Hacker
Rank

Sample Output
Hce akr
Rn ak
"""


for i in range(int(input())):
    s = input()
    print(s[::2], s[1::2])


"""
for i in range(int(input())):
    odd = ''
    even = ''
    s = input()
    for j in range(len(s)):
        if not j % 2:
            odd += s[j]
        else:
            even += s[j]
    print(odd, even)
"""


"""
t = int(input())
for i in range(0, t):
    odd = ''
    even = ''
    s = input()
    for j in range(0, len(s), 2):
        odd += s[j]
    for j in range(1, len(s), 2):
        even += s[j]
    print(odd, even)
"""