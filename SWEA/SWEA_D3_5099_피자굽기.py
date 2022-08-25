from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    C_list = list(map(int, input().split()))
    oven = deque()

    idx = 0
    for i in range(N):
        idx = i
        oven.append((C_list[idx], idx))

    while len(oven) > 1:
        c = oven.popleft()

        if c[0] // 2:
            oven.append((c[0] // 2, c[1]))

        if len(oven) < N and idx+1 < M:
            idx += 1
            oven.append((C_list[idx], idx))

    print('#{}'.format(tc), oven.popleft()[1]+1)