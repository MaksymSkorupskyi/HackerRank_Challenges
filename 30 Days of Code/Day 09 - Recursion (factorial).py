"""Day 9: Recursion 3

https://www.hackerrank.com/challenges/30-recursion/problem

Write a factorial function that takes a positive integer, n
as a parameter and prints the result of n! ( factorial).
"""


def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    n = int(input('Enter a number: ').strip())
    result = factorial(n)
    print(result)
