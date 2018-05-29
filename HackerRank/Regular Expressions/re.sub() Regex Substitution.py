"""Regex Substitution

https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

You are given a text of N lines. The text contains && and || symbols.
Your task is to modify those symbols to the following:
&& → and
|| → or
Both && and || should have a space " " on both sides.

Input Format
The first line contains the integer, n.
The next n lines each contain a line of the text.

Constraints
Neither && nor || occur in the start or end of each line.

Output Format
Output the modified text.

Sample Input:

11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b))
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.

Sample Output:

a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b))
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
"""

# text = ['x  & &&| && ||  ||  |x', 'n && && && && && &&n || || || || ||n', 'n || || || || ||n', 'if a + b > 0 && a - b < 0:', 'elif a*b > 10 || a/b < 1:', 'print set(list(a)) | set(list(b)) ', '#Note do not change &&& or ||| or & or |', "#Only change those '&&' which have space on both sides.", "#Only change those '|| which have space on both sides."]

# v1: lambda
import re
for i in range(int(input())):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))


# v2
import re

def and_or(match):
    if match.group() == "&&":
        return "and"
    else:
        return "or"


text = [input() for i in range(int(input()))]
for i in text:
    print(re.sub(r"(?<= )(&&|\|\|)(?= )", and_or, i))

    # print(re.sub(r"(?:^|(?<=\s))&&(?=\s|$)|(?:^|(?<=\s))\|\|(?=\s|$)", and_or, i))