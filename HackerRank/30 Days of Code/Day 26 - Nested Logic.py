"""Day 26: Nested Logic

https://www.hackerrank.com/challenges/30-nested-logic/problem

Your local library needs your help! Given the expected and actual return dates for a library book,
create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0.
If the book is returned after the expected return day but still within the same calendar month and year
as the expected return date, fine = 15 hackos * (the number of days late).
If the book is returned after the expected return month but still within the same calendar year
as the expected return date, the fine = 500 hackos * (the number of months late).
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 hackos.

Input Format

The first line contains 3 space-separated integers denoting the respective Day, Month, and Year
on which the book was actually returned.
The second line contains 3 space-separated integers denoting the respective Day, Month, and Year
on which the book was expected to be returned (due date).


Output Format
Print a single integer denoting the library fine for the book received as input.

Sample Input
9 6 2015
6 6 2015

Sample Output
45
"""

def fine(actual, expected):
    if actual[2] > expected[2]:
        return 10000
    if actual[1] > expected[1] and actual[2] == expected[2]:
        return 500 * (actual[1] - expected[1])
    if actual[0] > expected[0] and actual[1] == expected[1]:
        return 15 * (actual[0] - expected[0])
    return 0

# actual = list(map(int, sys.stdin.readline().split()))
# expected = list(map(int, sys.stdin.readline().split()))
# print(fine(actual, expected))


print(fine([9, 6, 2015], [6, 6, 2015]))
print(fine([9, 6, 2016], [6, 6, 2015]))
print(fine([9, 6, 2014], [6, 6, 2015]))
print(fine([9, 4, 2015], [6, 6, 2015]))
print(fine([1, 4, 2015], [6, 6, 2015]))