"""Day 0: Mean, Median, and Mode
https://www.hackerrank.com/challenges/s10-basic-statistics/problem

Given an array, X, of N integers, calculate and print the respective
mean, median, and mode on separate lines.
If your array contains more than one modal value, choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer),
your answers should be in decimal form, rounded to a scale of  decimal place (i.e., ,  format).

Input Format
The first line contains an integer, , denoting the number of elements in the array.
The second line contains  space-separated integers describing the array's elements.

Output Format

Print 3 lines of output in the following order:

Print the mean on a new line, to a scale of  decimal place (i.e., , ).
Print the median on a new line, to a scale of  decimal place (i.e., , ).
Print the mode on a new line; if more than one such value exists, print the numerically smallest one.

Sample Input:
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

Sample Output:
43900.6
44627.5
4978

Explanation

Mean:
We sum all  elements in the array, divide the sum by , and print our result on a new line.

Median:
To calculate the median, we need the elements of the array to be sorted in either non-increasing
or non-decreasing order. The sorted array . We then average the two middle elements:
and print our result on a new line.

Mode:
We can find the number of occurrences of all the elements in the array:
 4978 : 1
11735 : 1
14216 : 1
14470 : 1
38120 : 1
51135 : 1
64630 : 1
67060 : 1
73429 : 1
99233 : 1
Every number occurs once, making  the maximum number of occurrences for any number in X.
Because we have multiple values to choose from, we want to select the smallest one, 4978,
and print it on a new line.
"""

x = [4978, 64630, 14216, 14470,
     38120, 51135,
     64630, 67060, 64630, 51135, 1, 1, 1, 64630, 1]

from collections import Counter
# from scipy import stats

n = int(input())
x = sorted(map(int, input().split()))

print(round(sum(x)/len(x), 1))

if len(x) % 2:
    print(round(x[int((len(x)) / 2)], 1))
else:
    print(round((x[int((len(x)) / 2) -1] + x[int((len(x)) / 2)]) / 2, 1))

print(Counter(x).most_common()[0][0])

# print(int(stats.mode(x)[0]))



from collections import Counter

n = int(input())
x = sorted([int(i) for i in input().split()])

Mean = sum(x)/n
Median = (x[n // 2] + x[-(n//2 + 1)]) / 2
Mode = sorted(sorted(Counter(x).items()), key = lambda x: x[1], reverse = True)[0][0]

print(Mean, Median, Mode, sep = '\n')