"""No Idea!

https://www.hackerrank.com/challenges/no-idea/problem

There is an array of n integers. There are also 2 disjoint sets, A and B, each containing  integers.
You like all the integers in set  and dislike all the integers in set .
Your initial happiness is . For each  integer in the array, if , you add  to your happiness.
If i in B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

Input Format
The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format
Output a single integer, your total happiness.

Sample Input
3 2
1 5 3
3 1
5 7

Sample Output
1
"""

# v1
n, m = input().split()
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(sum((i in A) - (i in B) for i in arr)) # True == 1 and False == 0, nice!


# v2
n, m = map(int, input().split())
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happiness = 0
for i in arr:
        if i in a:
            happiness += 1
        elif i in b:
            happiness -= 1
print(happiness)