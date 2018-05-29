"""Set .difference()

.difference()
The tool .difference() returns a set with all the elements from the set that are not in an iterable.
Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
Set is immutable to the .difference() operation (or the - operation).

Task:
The students of District College have subscriptions to English and French newspapers.
Some students have subscribed only to English, some have subscribed to only French
and some have subscribed to both newspapers.

You are given two sets of student roll numbers.
One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper.
The same student could be in both sets.
Your task is to find the total number of students who have subscribed to only English newspapers.
"""

# v1 -
input()
english = set(input().split())
input()
french = set(input().split())
print(len(english - french))


# v2 .difference()
input()
english = set(input().split())
input()
french = set(input().split())
print(len(english.difference(french)))