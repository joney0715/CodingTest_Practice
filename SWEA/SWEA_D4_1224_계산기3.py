import sys

sys.stdin = open('input.txt', 'r')
T = 10

isp = {'+': 1, '*': 2, ')': 0, '(': 0}
icp = {'+': 1, '*': 2, ')': 0, '(': 3}

for tc in range(1, T + 1):
    N = int(sys.stdin.readline())
    cal = sys.stdin.readline().rstrip()

    stack = []
    result = ''
    for char in cal:
        if char.isdigit():
            result += char

        elif char == ')':
            while stack:
                if stack[-1] == '(':
                    break
                result += stack.pop()
            stack.pop()

        else:
            while stack:
                if icp.get(char) > isp.get(stack[-1]):
                    break
                result += stack.pop()
            stack.append(char)
    while stack:
        result += stack.pop()

    for a in result:
        if a.isdigit():
            stack.append(a)
        else:
            if a == '*':
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif a == '+':
                stack.append(int(stack.pop()) + int(stack.pop()))

    print('#{} {}'.format(tc, stack[0]))
