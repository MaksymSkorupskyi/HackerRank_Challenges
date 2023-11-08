"""Day 11: 2D Arrays
https://www.hackerrank.com/challenges/30-2d-arrays/problem

Context
Given a 2x2 2D Array, A:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in A to be a subset of values with indices falling in this pattern
in A's graphical representation:

a b c
  d
e f g
There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.
"""


arr = []

# for arr_i in range(6):
#    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#    arr.append(arr_t)

arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]

hourglass = -1000  # if array contains negative values
count = 0

for i in range(0, 4):
    for j in range(0, 4):
        count = arr[i][j] + arr[i][j+1] + arr[i][j+2] \
                            + arr[i+1][j+1] \
                + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if hourglass < count:
            hourglass = count

print(hourglass)