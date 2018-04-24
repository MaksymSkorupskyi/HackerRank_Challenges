"""Day 3: Intro to Conditional Statements

https://www.hackerrank.com/challenges/30-conditional-statements/problem

Given a positive integer, n, perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range 2 of 5 to , print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.
"""

n = int(input().strip())

if n % 2:
    print('Weird')
elif n in (2, 4) or n > 20:
    print('Not Weird')
else:
    print('Weird')


"""
n = int(input().strip())

if n % 2 != 0:
    print('Weird')
elif (n >= 2 and n <= 5) or n > 20:
    print('Not Weird')
else:
    print('Weird')
"""