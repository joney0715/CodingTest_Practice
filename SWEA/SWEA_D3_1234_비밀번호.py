# 1234_비밀번호
# 2022-08-18

import sys

sys.stdin = open('input_1234.txt', 'r')

for tc in range(1, 11):
    N, P = sys.stdin.readline().split()
    N = int(N)
    t = 0
    while True:
        cnt = 0
        for _ in P:
            cnt += 1
        P = list(P)

        i = 1
        while i < cnt:
            if P[i-1] == P[i]:
                P[i-1] = ''
                P[i] = ''
                break
            i += 1
        P = ''.join(P)

        if t == cnt:
            break
        t = cnt
        
    print('#{}'.format(tc), P)
    