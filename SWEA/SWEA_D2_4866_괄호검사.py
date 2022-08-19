# 4866_괄호검사
# 2022-08-18

T = int(input())

for tc in range(1, T+1):
    string = input()

    stack = []
    for char in string:
        if char == '(' or char == '{':
            stack.append(char)
        elif char == ')' or char == '}':
            if stack:
                a = stack.pop()
                if a == '(' and char == '}':
                    print('#{}'.format(tc), 0)
                    break
                elif a == '{' and char == ')':
                    print('#{}'.format(tc), 0)
                    break
            else:
                print('#{}'.format(tc), 0)
                break
    else:
        if stack:
            print('#{}'.format(tc), 0)
        else:
            print('#{}'.format(tc), 1)