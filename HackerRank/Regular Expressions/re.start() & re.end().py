"""Re.start() & Re.end()

You are given a string s.
Your task is to find the indices of the start and end of string k in .

Input Format
The first line contains the string s.
The second line contains the string k.

Output Format
Print the tuple in this format: (start_index, end_index).
If no match is found, print (-1, -1).

Sample Input
aaadaa
aa

Sample Output
(0, 1)
(1, 2)
(4, 5)

"""

import re

s = input()
k = input()
if k in s:
    print(*[(i.start(), (i.start() + len(k) - 1)) for i in re.finditer(r'(?={})'.format(k), s)], sep='\n')
else:
    print('(-1, -1)')
