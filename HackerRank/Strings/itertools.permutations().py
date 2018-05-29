from itertools import permutations

# s = 'HACK'
# n = 2

s, n = input().split()

for i in permutations(sorted(s), int(n)):
    print(*i, sep='')

# one-liner

# print(*[''.join(i) for i in permutations(sorted(s), int(n))], sep='\n')