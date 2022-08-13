T = int(input())

for tc in range(1,T+1):
    N = int(input())
    trade_list = list(map(int, input().split()))

    buy = 0
    profit = 0
    idx_max = k = 0
    while True:
        for i in range(idx_max,  N):
            if trade_list[idx_max] < trade_list[i]:
                idx_max = i

        for j in range(k, N):
            if j == idx_max:
                profit += buy * trade_list[j]
                buy = 0
                break
            else:
                buy += 1
                profit -= trade_list[j]
        if idx_max == N-1:
            break
        idx_max += 1
        k = idx_max
    print('#{}'.format(tc), profit)