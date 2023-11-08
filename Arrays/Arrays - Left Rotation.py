def array_left_rotation(a, n, k):
    return a[k:] + a[:k]

# def array_left_rotation(a, n, k):
    # if k != n:
    #     for i in range(k):
    #         a.append(a.pop(0))
    # return a


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k)
print(*answer, sep=' ')
