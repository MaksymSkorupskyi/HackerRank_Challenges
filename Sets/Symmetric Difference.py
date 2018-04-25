"""Symmetric Difference

Given  sets of integers,  and , print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format

The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.
"""

input()
A = set(map(int, input().split()))
input()
B = set(map(int, input().split()))
print(*sorted(A ^ B), sep='\n')