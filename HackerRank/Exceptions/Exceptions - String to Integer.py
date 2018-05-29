"""Day 16: Exceptions - String to Integer

https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem

Read a string, s, and print its integer value; if s cannot be converted to an integer, print Bad String.

Note: You must use the String-to-Integer and exception handling constructs built into your submission language.
If you attempt to use loops/conditional statements, you will get a 0 score.
"""

# v1
try:
    print(int(input().strip()))
except ValueError:
    print('Bad String')


# v2, with variable s
s = input().strip()
try:
    print(int(s))
except ValueError:
    print('Bad String')
