"""Lists

Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands
where each command will be of the  types listed above.
Iterate through each command in order and perform the corresponding operation on your list.

Input Format
The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints
The elements added to the list must be integers.

Output Format
For each command of type print, print the list on a new line.

Sample Input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

# v1: if elif
a = []
for i in range(int(input())):
    command = input().split()
    if command[0] == 'print':
        print(a)
    elif command[0] == 'sort':
        a.sort()
    elif command[0] == 'pop':
        a.pop()
    elif command[0] == 'reverse':
        a.reverse()
    elif command[0] == 'insert':
        a.insert(int(command[1]), int(command[2]))
    elif command[0] == 'remove':
        if int(command[1]) in a:
            a.remove(int(command[1]))
    elif command[0] == 'append':
        a.append(int(command[1]))

# v2: eval() - bad practice
a = []
for i in range(int(input())):
    command = input().split()
    if command[0] =='print':
        print(a)
    else:
        eval('a.' + command[0] + '(' + ','.join(command[1:]) + ')')

# v3: getattr()
a = []
for i in range(int(input())):
    command = input().split()
    if command[0] == 'print':
        print(a)
    else:
        getattr(a, command[0])(*map(int, command[1:]))

# v4: getattr() + list comprehensions
a = []
[getattr(a, command[0])(*map(int, command[1:])) if hasattr(a, command[0]) else print(a) for command in
 [input().split() for i in range(int(input()))]]