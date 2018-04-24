"""Day 19: Interfaces

https://www.hackerrank.com/challenges/30-interfaces/problem
The AdvancedArithmetic interface and the method declaration for the abstract divisorSum(n) method
are provided for you in the editor below.

Complete the implementation of Calculator class, which implements the AdvancedArithmetic interface.
The implementation for the divisorSum(n) method must return the sum of all divisors of n.

Sample Input
6

Sample Output
I implemented: AdvancedArithmetic
12
"""


class AdvancedArithmetic():
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        result = n
        for i in range(1, n // 2 + 1): # finding all divisors of n
            if not n % i:
                result += i
        return result


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
