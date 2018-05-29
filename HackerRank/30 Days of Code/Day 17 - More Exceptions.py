"""Day 17: More Exceptions

https://www.hackerrank.com/challenges/30-more-exceptions/problem

Write a Calculator class with a single method: int power(int,int).
The power method takes two integers, n and p, as parameters and returns the integer result of .
If either n or p is negative, then the method must throw an exception with the message:
'n and p should be non-negative'.

Note: Do not use an access modifier (e.g.: public) in the declaration for your Calculator class.

Sample Input
4
3 5
2 4
-1 -2
-1 3

Sample Output
243
16
n and p should be non-negative
n and p should be non-negative
"""


class Calculator:
    def __init__(self):
        pass

    # since the method does not reference any class or instance attributes,
    # you could make it a static method by using the @staticmethod decorator,
    # which provides more flexibility by allowing you to call the method without creating a Calculator instance.
    @staticmethod
    def power(n, p):
        if n < 0 or p < 0:
            raise (Exception('n and p should be non-negative'))
        return n ** p


# myCalculator = Calculator()
for i in range(int(input())):
    n, p = map(int, input().split())
    try:
        # ans = myCalculator.power(n, p)
        print(Calculator.power(n, p))
    except Exception as e:
        print(e)
