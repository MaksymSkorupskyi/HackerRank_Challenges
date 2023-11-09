"""Day 25 - Running Time and Complexity (prime numbers)

https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself.
Given a number, n, determine and print whether it's Prime or Not prime.

Note: If possible, try to come up with a O(√n) primality algorithm,
or see what sort of optimizations you come up with for an  algorithm.
"""


def isprime(self):
    if self <= 1:
        return False
    if self in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97):
        return True
    for i in range(2, round(self ** 0.5) + 1):
        if self % i == 0:
            return False

    return True


for i in range(int(input())):
    if isprime(int(input())):
        print('Prime')
    else:
        print('Not prime')

# my first code - very straightforward :)
# def isprime(self):
#     if self <= 1:
#         print('Not prime')
#     elif self in (2, 3):
#         print('Prime')
#     else:
#         for i in range(2, round(self ** 0.5) + 1):
#             if self % i == 0:d
#                 print('Not prime')
#                 return
#         print('Prime')
#
#
# for i in range(int(input())):
#     isprime(int(input()))

# for i in range(100):
#     print(i, round(i ** 0.5))
#     isprime(i)
