from collections import *
a = Counter(input())
b = Counter(input())
c = a - b
d = b - a
e = c + d
print(len(list(e.elements())))

def number_needed(a, b):
    total = 0
    for letter in "abcdefghijklmnopqrstuvwxyz":
        total += abs(a.count(letter) - b.count(letter))
    return total

def number_needed(a, b):
    count = 0
    a_set = set(a)
    b_set = set(b)
    for i in a_set - b_set:
        count += a.count(i)
    for j in b_set - a_set:
        count += b.count(j)
    for k in a_set & b_set:
        count += abs(a.count(k) - b.count(k))
    return count

    # print(sorted(a_set), sorted(a_set - b_set))
    # print(sorted(b_set), sorted(b_set - a_set))
    # print(sorted(a_set & b_set))
    # print(sorted(a_set | b_set))
    # print(sorted(a_set ^ b_set))


# a = input().strip()
# b = input().strip()

print(number_needed('abcf', 'cdcecf'))