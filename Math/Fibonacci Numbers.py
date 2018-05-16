# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem


# v1: cycle, fast
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# v2: recursion, very slow with large n
def fibonacci(n):
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input())
print(fibonacci(n))
