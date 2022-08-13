T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    max_value = 0
    mapping = [list(map(int, input().split())) for _ in range(N)]
    # 가로
    for i in range(N):
        count = 0
        for j in range(M):
            if mapping[i][j] == 1:
                count += 1
                if max_value < count:
                    max_value = count
            else:
                count = 0
    # 세로
    for i in range(M):
        count = 0
        for j in range(N):
            if mapping[j][i] == 1:
                count += 1
                if max_value < count:
                    max_value = count
            else:
                count = 0
    print('#{}'.format(tc), max_value)
                                    
                                                                        