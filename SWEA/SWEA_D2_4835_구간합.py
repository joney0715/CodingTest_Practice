# 4835_구간합
# 220809

def n_sum(N_list, s, e):
    N_sum = 0
    for j in range(e):
        N_sum += N_list[s+j]
    return N_sum

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    N_list = list(map(int, input().split()))

    N_min = N_max = n_sum(N_list, 0, M)
    for i in range(N-M+1):
        N_sum = n_sum(N_list, i, M)
        if N_min > N_sum:
            N_min = N_sum
        if N_max < N_sum:
            N_max = N_sum

    print(f'#{tc} {N_max - N_min}')
