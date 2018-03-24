n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

weighted = 0
for i in range(len(x)):
    weighted += x[i] * w[i]

print(round(weighted/sum(w), 1))



#
N = map(int,input().split())
X = list(map(int, input().strip().split(' ')))
W = list(map(int, input().strip().split(' ')))
sum_X = sum([a*b for a,b in zip(X,W)])
print(round((sum_X/sum(W)),1))
