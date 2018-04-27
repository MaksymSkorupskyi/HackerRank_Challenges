"""Print Function

Read an integer N.
Without using any string methods, try to print the following:
123...N

"""

n = int(input())
print(*range(1, n+1), sep='')

# print(*range(1, int(input())+1), sep='')