x = [1, 3, 5, 7, 8, 12, 13, 14, 18, 21]

def median(x):
    if len(x) % 2:
        return x[len(x) // 2]
    else:
        return (x[len(x) // 2 - 1] + x[len(x) // 2]) / 2

# n = input()
# x = sorted(map(int, input().split()))
Q1 = median(x[:len(x) // 2])
Q2 = median(x)
Q3 = median(x[-(len(x) // 2):])
print(int(Q1), int(Q2), int(Q3), sep='\n')

print(int(median(x[:len(x) // 2])), int(median(x)), int(median(x[- (len(x) // 2):])), sep='\n')



print(x[:len(x) // 2])
print(x[- (len(x) // 2):])
print(len(x), len(x) // 2, x, int(median(x[:len(x) // 2])), int(median(x)), int(median(x[len(x) // 2:])), sep='\n')

