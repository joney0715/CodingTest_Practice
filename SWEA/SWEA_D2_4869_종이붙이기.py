# 4869_종이붙이기
# 2022-08-18

T = int(input())

N_list = [0] * 31
N_list[1] = 1
N_list[2] = 3

for tc in range(1, T+1):
    N = int(input())

    N //= 10

    for n in range(3,N+1):
        N_list[n] = N_list[n-1] + N_list[n-2] * 2

    print('#{}'.format(tc), N_list[N])
