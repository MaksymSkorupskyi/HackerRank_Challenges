# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem

# recursion
def fibonacci(n):
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


# cycle
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

n = int(input())
print(fibonacci(n))
