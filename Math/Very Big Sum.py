"""Very Big Sum

https://www.hackerrank.com/challenges/a-very-big-sum/problem

Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

Input Format

The first line of the input consists of an integer n.
The next line contains n space-separated integers contained in the array.

Output Format
Print the integer sum of the elements in the array.


Sample Input
5
1000000001 1000000002 1000000003 1000000004 1000000005

Output
5000000015
"""

import os

def aVeryBigSum(n, ar):
    return sum(ar)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(n, ar)
    f.write(str(result) + '\n')
    f.close()