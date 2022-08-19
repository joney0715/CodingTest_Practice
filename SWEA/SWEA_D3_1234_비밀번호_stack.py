# 1234_비밀번호
# 2022-08-18

import sys

sys.stdin = open('input_1234.txt', 'r')

for tc in range(1, 11):
    N, P = sys.stdin.readline().split()
    N = int(N)
    length = 0

    for _ in P:
        length += 1

    stack = [P[0]]
    for i in range(1,length):
        if stack:
            if P[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(P[i])
        else:
            stack.append(P[i])
        
    answer = ''.join(stack)
        
    print('#{}'.format(tc), answer)