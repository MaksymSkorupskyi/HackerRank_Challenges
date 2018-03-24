s = S = 'qA2'

print(any(x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' for x in s))
print(any(x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for x in s))
print(any(x in '0123456789' for x in s))
print(any(x in 'abcdefghijklmnopqrstuvwxyz' for x in s))
print(any(x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for x in s))

print(any([char.isalnum() for char in S]))
print(any([char.isalpha() for char in S]))
print(any([char.isdigit() for char in S]))
print(any([char.islower() for char in S]))
print(any([char.isupper() for char in S]))