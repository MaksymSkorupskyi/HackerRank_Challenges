"""Day 4: Binomial Distribution II
https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

A manufacturer of metal pistons finds that, on average,
12% of the pistons they manufacture are rejected because they are incorrectly sized.
What is the probability that a batch of 10 pistons will contain:
1) No more than 2 rejects?
2) At least 2 rejects?
"""

def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


def binomial_coefficient(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def binomial_distribution_exact(k, n, p): # = k
    return binomial_coefficient(n, k) * (p ** k) * ((1 - p) ** (n - k))


def binomial_distribution_at_least(k, n, p): # >= k
    binomial_distribution = 0
    for i in range(k, n + 1):
        binomial_distribution += binomial_coefficient(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return binomial_distribution

def binomial_distribution_at_most(k, n, p): # <=k
    binomial_distribution = 0
    for i in range(k + 1):
        binomial_distribution += binomial_coefficient(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return binomial_distribution


"""
n - total number of trials. The trials are independent.
p - probability of success of 1 trial
q=1-p - probability of failure of 1 trial, where q = 1 - p.
k - number of successes
find b, The binomial random variable is the number of successes k, out of n trials.
"""

p, n = map(int, input().split())
k = 2
if p > 1:
    p = p / 100
print(round(binomial_distribution_at_most(k, n, p), 3))
print(round(binomial_distribution_at_least(k, n, p), 3))


print(binomial_distribution_exact(5, 10, 1/2))
print(binomial_distribution_at_least(5, 10, 1/2))
print(binomial_distribution_at_most(5, 10, 1/2))
print(binomial_distribution_exact(3, 6, 1.09 / (1.09 + 1)))
print(binomial_distribution_at_least(3, 6, 1.09 / (1.09 + 1)))
print(binomial_distribution_at_most(3, 6, 1.09 / (1.09 + 1)))