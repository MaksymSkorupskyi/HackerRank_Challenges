x = [6, 12, 8, 10, 20, 16]
f = [5, 4, 3, 2, 1, 5]

def median(x):
    if len(x) % 2:
        return x[len(x) // 2]
    else:
        return (x[(len(x) // 2) - 1] + x[len(x) // 2]) / 2

n = input()
x = list(map(int, input().split()))
f = list(map(int, input().split()))
s = []
for i in range(len(x)):
    s += [x[i]] * f[i]
s.sort()
Q1 = median(s[:len(s) // 2])
Q3 = median(s[-(len(s) // 2):])
print(round(float(Q3-Q1), 1))

print("%.1f" % round(Q3 - Q1, 1)) # represent it with only one digit !!!



print(Q1, Q3, Q3-Q1, x, f, len(s), s, sep='\n')


"""
https://github.com/python/cpython/blob/3.6/Lib/statistics.py

def median(data):
    data = sorted(data)
    n = len(data)
    if n == 0:
        raise StatisticsError("no median for empty data")
    if n%2 == 1:
        return data[n//2]
    else:
        i = n//2
        return (data[i - 1] + data[i])/2
"""