def is_matched(expression):
    brackets = {'{': 1, '}': -1,
                '[': 2, ']': -2,
                '(': 4, ')': -4}
    stack = []
    for i in expression:
        if brackets[i] > 0:
            stack.append(brackets[i])
        elif stack and stack[-1] + brackets[i] == 0:
            stack.pop()
        else:
            return False
    return not stack


# print(is_matched('{[(])}'))

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression):
        print("YES")
    else:
        print("NO")