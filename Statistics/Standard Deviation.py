x = [10, 40, 30, 50, 20]

n = input()
x = list(map(int, input().split()))
mean = sum(x)/len(x)
variance = sum((i - mean) ** 2 for i in x) / len(x)
standard_deviation = variance ** 0.5
print(round(standard_deviation, 1))


print(standard_deviation, mean, variance, x, sep='\n')