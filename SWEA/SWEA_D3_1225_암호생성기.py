# 1225_암호 생성기
# 2022-08-24

import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(sys.stdin.readline())

    N_list = list(map(int, sys.stdin.readline().split()))

    i = 1
    while True:
        n = N_list[0]
        for j in range(1, 8):
            N_list[j-1] = N_list[j]
        
        if n - i <= 0:
            N_list[7] = 0
            break
        else:
            N_list[7] = n - i

        if i == 5:
            i = 1
        else:
            i += 1

    print('#{}'.format(tc), *N_list)

