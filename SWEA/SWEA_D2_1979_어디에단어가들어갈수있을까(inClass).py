# 1979_어디에 단어가 들어갈 수 있을까
# 2022-08-11

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
  
    row = col = 0
    count = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                row += 1
            else:
                if row == K:
                    count += 1
                row = 0

            if maps[j][i] == 1:
                col += 1
            else:
                if col == K:
                    count += 1
                col = 0

        if row == K:
            count += 1
        row = 0

        if col == K:
            count += 1
        col = 0
    
    print(f'#{test_case}', count)