"""Nested Lists

Given the names and grades for each student in a Physics class of  students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note:
If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format
The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines;
the first line contains a student's name, and the second line contains their grade.

Constraints
There will always be one or more students having the second lowest grade.

Output Format
Print the name(s) of any student(s) having the second lowest grade in Physics;
if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0
Berry
Harry

Explanation 0
There are  students in this class whose names and grades are assembled to build the following list:
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of  belongs to Tina.
The second lowest grade of  belongs to both Harry and Berry,
so we order their names alphabetically and print each name on a new line.
"""

# v1 My 1st solution using dict() :)))
students_dict = {}
first_lowest_grade = second_lowest_grade = 100
for i in range(int(input())):
    name = input()
    score = float(input())
    if score < second_lowest_grade:
        if score < first_lowest_grade:
            second_lowest_grade = first_lowest_grade
            first_lowest_grade = score
        elif first_lowest_grade != score:
            second_lowest_grade = score
    students_dict[name] = score
print(*sorted([k for k, v in students_dict.items() if v == second_lowest_grade]), sep='\n')

# v2
grades = [[input(), float(input())] for _ in range(int(input()))]
second_highest = sorted(list(set([score for name, score in grades])))[1]
print(*[a for a, b in sorted(grades) if b == second_highest], sep='\n')

# v3
grades = sorted([[input(), float(input())] for _ in range(int(input()))])
scores = sorted(list(set([s for _, s in grades])))
[print(n) for n, s in grades if s == scores[1]]

# v4 two-liner

grades = sorted([[input(), float(input())] for i in range(int(input()))])
print(*[x for x, y in grades if y == sorted(set([score for name, score in grades]))[1]], sep='\n')

# print(grades)