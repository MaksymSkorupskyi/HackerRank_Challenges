"""Day 4: Binomial Distribution I
https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

The ratio of boys to girls for babies born in Ukraine is 1,09 : 1.
If there is 1 child born per birth,
what proportion of Ukrainian families with exactly 6 children will have at least 3 boys?

Input Format

A single line containing the following values:
1.09 1

Output Format

Print a single line denoting the answer, rounded to a scale of  decimal places (i.e., 1.234 format).
"""


def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

"""The ratio of boys to girls for babies born in Ukraine is 1.09 : 1. 
If there is 1 child born per birth, 
what proportion of ukrainian families with exactly 6 children will have AT LEAST 3 boys?
"""
n = 6  # total number of trials. The trials are independent.
p = 1.09 / (1.09 + 1) # probability of success of 1 trial, in this case: boy has been born
q = 1 - p # probability of failure of 1 trial, where q = 1 - p.
x = 3   # number of successes
# find b, The binomial random variable is the number of successes x, out of n trials.

# x >= 3, Getting AT LEAST x successes.
binomial_distribution = 0
for i in range (x, n + 1):
    binomial_coefficient = factorial(n) / (factorial(i) * factorial(n - i))
    binomial_distribution += binomial_coefficient * (p ** i) * (q ** (n - i))
print(round(binomial_distribution, 3))


"""
A fair coin is 10 tossed  times. Find the following probabilities:
Getting 5 heads.
Getting at least 5  heads.
Getting at most 5 heads.
"""
"""
n = 10  # total number of trials. The trials are independent.
p = 1/2 # probability of success of 1 trial
q = 1 - p # probability of failure of 1 trial, where q = 1 - p.
x = 5   # number of successes
# find b, The binomial random variable is the number of successes x, out of n trials.

# x = 5, Getting EXACTLY x successes.
binomial_coefficient = factorial(n) / (factorial(x) * factorial(n - x))
binomial_distribution = binomial_coefficient * (p ** x) * (q ** (n - x))
print(binomial_distribution)

# x >= 5, Getting AT LEAST x successes.
binomial_distribution = 0
for i in range (x, n + 1):
    binomial_coefficient = factorial(n) / (factorial(i) * factorial(n - i))
    binomial_distribution += binomial_coefficient * (p ** i) * (q ** (n - i))
print(binomial_distribution)

# x <= 5, Getting AT MOST x successes.
binomial_distribution = 0
for i in range (x + 1):
    binomial_coefficient = factorial(n) / (factorial(i) * factorial(n - i))
    binomial_distribution += binomial_coefficient * (p ** i) * (q ** (n - i))
print(binomial_distribution)
"""



