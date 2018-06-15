"""Class 2 - Find the Torsional Angle

https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem

You are given four points A, B, C and D in the 3-dimensional cartesian coordinate system.
You are required to print the angle between the plane made by points A, B, C and B, C, D in degrees(NOT RADIAN).
Let the angle be PHI.
Cos(PHI) = (X . Y)/|X||Y| where X = AB x BC and Y = BC x CD.
Here X.Y means the dot product of X and Y.
AB x BC means the cross product of vectors AB and BC. AB = B - A.

Input Format
X, Y and Z coordinates of a point in one line separated by space, where they are floating numbers.

Output Format
Angle with precision of two digits after decimal.

Sample Input
0 4 5
1 7 6
0 5 9
1 7 2

Sample Output
8.19
"""

import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        pass

    def dot(self, no):
        pass

    def cross(self, no):
        pass

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    print(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))