# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem
from functools import lru_cache


# v1: cycle, fast
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# v2: recursion, very slow with large n
def fibonacci(n):
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# v3: recursion, optimized
def fibonacci(n):
    if n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    return n


# v4: recursion, optimized
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# generator
# def fibonacci(n):
#     a, b = 0, 1
#     while a < n:
#         yield a
#         a, b = b, a + b


n = int(input())
print(fibonacci(n))
