T = int(input())
for tc in range(1, T + 1):
    cal = list(input().split())

    stack = []
    for char in cal:
        if char == '.':
            if len(stack) == 1:
                print('#{}'.format(tc), stack.pop())
            else:
                print('#{}'.format(tc), 'error')

        elif char.isdigit():
            stack.append(char)

        else:
            if len(stack) < 2:
                print('#{}'.format(tc), 'error')
                break
            else:
                b = int(stack.pop())
                a = int(stack.pop())

                if str(a).isdigit() and str(b).isdigit():
                    if char == '+':
                        stack.append(a + b)
                    elif char == '-':
                        stack.append(a - b)
                    elif char == '/':
                        stack.append(a // b)
                    elif char == '*':
                        stack.append(a * b)
                else:
                    print('#{}'.format(tc), 'error')
                    break
