n = 98

# n = int(input())
w = len(format(n, 'b'))
for i in range(1, n + 1):
    print(str(i).rjust(w), format(i, 'o').rjust(w), format(i, 'X').rjust(w), format(i, 'b').rjust(w))