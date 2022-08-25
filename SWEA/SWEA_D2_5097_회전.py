T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    N_list = list(map(int, input().split()))

    for i in range(M):
        n = N_list[0]

        for j in range(1, N):
            N_list[j-1] = N_list[j]

        N_list[N-1] = n

    print('#{}'.format(tc), N_list[0])
