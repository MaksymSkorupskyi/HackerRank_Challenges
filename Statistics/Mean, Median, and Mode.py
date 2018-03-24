x = [4978, 64630, 14216, 14470,
     38120, 51135,
     64630, 67060, 64630, 51135, 1, 1, 1, 64630, 1]

from collections import Counter
# from scipy import stats

n = int(input())
x = sorted(map(int, input().split()))

print(round(sum(x)/len(x), 1))

if len(x) % 2:
    print(round(x[int((len(x)) / 2)], 1))
else:
    print(round((x[int((len(x)) / 2) -1] + x[int((len(x)) / 2)]) / 2, 1))

print(Counter(x).most_common()[0][0])

# print(int(stats.mode(x)[0]))




from collections import Counter

n = int(input())
x = sorted([int(i) for i in input().split()])

Mean = sum(x)/n
Median = (x[n // 2] + x[-(n//2 + 1)]) / 2
Mode = sorted(sorted(Counter(x).items()), key = lambda x: x[1], reverse = True)[0][0]

print(Mean, Median, Mode, sep = '\n')