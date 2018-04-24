"""Day 14: Scope
https://www.hackerrank.com/challenges/30-scope/problem

"""

class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = (max(self.__elements) - min(self.__elements))


a = [1, 2, 5]

# print(max(a) - min(a))


d = Difference(a)
d.computeDifference()
print(d.maximumDifference)
