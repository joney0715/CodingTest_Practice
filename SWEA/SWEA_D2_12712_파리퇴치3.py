T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flies_map = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    for i in range(N):
        for j in range(N):
            dead_flies_2 = flies_map[i][j]
            dead_flies_1 = flies_map[i][j]
            for k in range(1,M):
                # 수직 수평 분사
                if j+k < N:
                    dead_flies_1 += flies_map[i][j+k]
                if 0 <= j-k:
                    dead_flies_1 += flies_map[i][j-k]
                if i+k < N:
                    dead_flies_1 += flies_map[i+k][j]
                if 0 <= i-k:
                    dead_flies_1 += flies_map[i-k][j]
                
                # 대각선 분사
                if i+k < N and j+k < N:
                    dead_flies_2 += flies_map[i+k][j+k]
                if i+k < N and 0 <= j-k:
                    dead_flies_2 += flies_map[i+k][j-k]
                if 0 <= i-k and 0 <= j-k:
                    dead_flies_2 += flies_map[i-k][j-k]
                if 0 <= i-k and j+k < N:
                    dead_flies_2 += flies_map[i-k][j+k]

                for v in [dead_flies_1,dead_flies_2]:
                    if max_value < v:
                        max_value = v

    print('#{}'.format(tc), max_value)
