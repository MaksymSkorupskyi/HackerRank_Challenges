"""Day 10: Binary Numbers
https://www.hackerrank.com/challenges/30-binary-numbers/problem

Given a base- integer, , convert it to binary (base-2).
Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

Input Format
A single integer, n.

Output Format
Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n.

Sample Input 1
5
Sample Output 1
1

Sample Input 2
13
Sample Output 2
2
"""

# one-liner:
print(len(max(bin(int(input().strip()))[2:].split('0'))))

"""for sake of explenation im going to replace input() with '13' and break the code down.
1- int(input().strip()) ==> int('13'.strip()) takes the input of the number and strips any spaces on either side, 
then converts it from a string to an interger. the result is the interger 13.

2- bin(13)[2:].split('0') ==> the bin() method takes a number and converts it to binary. 
in this case when you enter bin(13) it returns '0b1101'. 
the [2:] allows us to omit the '0b' at the beginning of the string. 
which leaves us with '1101'.split('0'). 
This string method takes '1101' and splits it into a list. 
We end up with ['11','1'].

3-len(max(['11','1'])) ==> the max() method is simply going to look for the biggest value. 
In this case the biggest one is '11'. 
'11' is passed to the len() method which just returns the length of the object in it. 
In this case the object is the string '11' which has two characters, so len('11') returns 2. 
Which in turn is also the longest consecutive amount of ones.
"""

# my first solution:
n = int(input().strip())
s = bin(n)[2:]  # s = "{0:b}".format(n)
count = 0
maxcount = 0
for i in s:
    if i == '1':
        count += 1
    else:
        count = 0
    if maxcount < count:
        maxcount = count
print(maxcount)