"""Day 16: Exceptions - String to Integer

https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem

Read a string, , and print its integer value; if  cannot be converted to an integer, print Bad String.

Note: You must use the String-to-Integer and exception handling constructs built into your submission language.
If you attempt to use loops/conditional statements, you will get a 0 score.
"""


s = input().strip()
try:
    print(int(s))
except ValueError:
    print('Bad String')
