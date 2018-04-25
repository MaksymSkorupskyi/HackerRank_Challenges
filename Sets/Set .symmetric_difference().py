"""Set .symmetric_difference()

The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
The set is immutable to the .symmetric_difference() operation (or ^ operation).

Task:
The students of District College have subscriptions to English and French newspapers.
Some students have subscribed only to English, some have subscribed to only French
and some have subscribed to both newspapers.

You are given two sets of student roll numbers.
One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper.
The same student could be in both sets.
Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.
"""

# v1 ^
input()
english = set(input().split())
input()
french = set(input().split())
print(len(english ^ french))


# v2 .symmetric_difference()
input()
english = set(input().split())
input()
french = set(input().split())
print(len(english.symmetric_difference(french)))