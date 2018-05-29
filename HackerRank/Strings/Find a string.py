"""Find a string
https://www.hackerrank.com/challenges/find-a-string/problem

In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.
NOTE: String letters are case-sensitive.

Input Format
The first line of input contains the original string. The next line contains the substring.
"""

import re


def count_substring(string, sub_string):
    return len(re.findall('(?=' + sub_string + ')', string))


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    print(count_substring(string, sub_string))