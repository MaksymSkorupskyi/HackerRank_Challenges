"""Day 29: Bitwise AND

Given set S = {1,2,3,...,N}.
Find two integers, A and B (where A < B), from set S such that the value of A&B is the maximum possible
and also less than a given integer, K. In this case, & represents the bitwise AND operator.

Input Format

The first line contains an integer, T, the number of test cases.
Each of the T subsequent lines defines a test case as 2 space-separated integers, N and K, respectively.

Output Format
For each test case, print the maximum possible value of  on a new line.

Sample Input
3
5 2
8 5
2 2

Sample Output
1
4
0
"""

for i in range(int(input())):
    n, k = map(int, input().split())
    if (k - 1) | k <= n:
        print(k - 1)
    else:
        print(k - 2)
"""        
When k is ODD , k-1 is EVEN , k-1 can always be reached by (k-1) & k.

In binary form:
    k   = 11
    k-1 = 10
    k-1 == (k-1) & k
That is , ((k-1) | k) is always k. And ((k-1) | k) <= n is always TRUE.
When k is EVEN , k-1 is ODD , k-1 can only be reached if and only if ((k-1) | k) <= n is TRUE

Why?
In binary form:
    k   = 10110
    k-1 = 10101
    pos = 10111
    k-1 == (k-1) & pos
You can get k-1 if pos <= n is TRUE. And you can get pos by ((k-1) | (k-1+1)) , that is , ((k-1) | k). 
Otherwise, you just need to follow the process above when k is ODD (because k-1 is ODD) , 
then you get the answer k-2.

In brief , you can just do the test ((k-1) | k) <= n to determine the answer.
"""


# Brute-force (Accepted)
def FindMaxAB(n, k):
    max_ab = 0
    for i in range(k - 2, n):
        for j in range(i + 1, n + 1):
            ab = i & j
            if ab == k - 1:
                return ab
            if max_ab < ab < k:
                max_ab = ab
    return max_ab


for i in range(int(input().strip())):
    n, k = map(int, input().split())
    print(FindMaxAB(n, k))