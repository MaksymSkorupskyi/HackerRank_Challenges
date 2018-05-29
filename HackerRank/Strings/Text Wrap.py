import textwrap

string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width = 4

# def wrap(string, max_width):
#     return textwrap.fill(string, max_width)
    # return '\n'.join(textwrap.wrap(string, max_width))

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)

for i in range(0, len(string), max_width):
    print(string[i:max_width + i])

# print(*textwrap.wrap(string, max_width), sep='\n')