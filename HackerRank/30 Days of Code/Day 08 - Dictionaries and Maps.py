"""Day 8: Dictionaries and Maps

https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
You will then be given an unknown number of names to query your phone book for.
For each  queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
if an entry for  is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input Format
The first line contains an integer, n, denoting the number of entries in the phone book.
Each of the  subsequent lines describes an entry in the form of  space-separated values on a single line.
The first value is a friend's name, and the second value is an -digit phone number.

After the  lines of phone book entries, there are an unknown number of lines of queries.
Each line (query) contains a to look up, and you must continue reading lines until there is no more input.

Note: Names consist of lowercase English alphabetic letters and are first names only.

Sample Input
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Sample Output
sam=99912222
Not found
harry=12299933
"""


import sys

n = int(input().strip())
phonebook = dict(input().split() for i in range(n))

for line in sys.stdin.readlines():
    line = line.strip()
    if line in phonebook:
        print('{0}={1}'.format(line, phonebook.get(line)))
    else:
        print('Not found')


"""
n = int(input().strip())
phonebook = dict(input().split() for i in range(n))
while True:
    try:
        query.append(input()) # next line was found
    except (EOFError):
        break #end of file reached
for i in range(len(query)):
    if query[i] in phonebook:
        print('{0}={1}'.format(query[i], phonebook.get(query[i])))
    else:
        print('Not found')
"""
# print(phonebook)
# print(query)