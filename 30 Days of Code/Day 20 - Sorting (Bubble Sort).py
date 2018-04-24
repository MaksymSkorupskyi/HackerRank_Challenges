"""Day 20: Sorting (Bubble Sort)

https://www.hackerrank.com/challenges/30-sorting/problem
Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm.
Once sorted, print the following  lines:

Array is sorted in numSwaps swaps.
where numSwaps is the number of swaps that took place.
First Element: firstElement
where firstElement is the first element in the sorted array.
Last Element: lastElement
where lastElement is the last element in the sorted array.
"""

# n = int(input().strip())
# a = list(map(int, input().strip().split(' ')))

n = 4
a = [4, 2, 3, 0]

numSwaps = 0
unsorted = True
passnumber = len(a) - 1

while unsorted:
    unsorted = False
    for i in range(passnumber):
        if a[i] > a[i + 1]:
            a[i + 1], a[i] = a[i], a[i + 1]
            numSwaps += 1
        unsorted = True
    passnumber -= 1

print('Array is sorted in', numSwaps, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])


"""
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwaps = 0

for i in range(n):
    numberOfSwaps = 0
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]
            numberOfSwaps += 1
            numSwaps += 1
    if numberOfSwaps == 0:
        break

print('Array is sorted in', numSwaps, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])
"""
