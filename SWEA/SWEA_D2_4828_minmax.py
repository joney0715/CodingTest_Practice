# 4828-min-max
# 2022-08-09

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    N_list = list(map(int, input().split()))

    N_min = N_max = N_list[0]
    for i in range(1,N):
        if N_min > N_list[i]:
            N_min = N_list[i]
        if N_max < N_list[i]:
            N_max = N_list[i]

    print('#{} {}'.format(tc, N_max - N_min))