"""Find the Median

https://www.hackerrank.com/challenges/find-the-median/problem
The median of a list of numbers is essentially it's middle element after sorting.
The same number of elements occur after it as before.
Given a list of numbers with an odd number of elements, can you find the median?
"""


def findMedian(arr):
    arr.sort()
    if len(arr) % 2:
        return arr[len(arr) // 2]
    return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = findMedian(arr)
    print(result)
