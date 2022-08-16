# 2001_파리 퇴치
# 2022-08-16

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flies_map = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            dead_fly = 0
            for x in range(0,M):
                for y in range(0,M):
                    dead_fly += flies_map[i+x][j+y]
            if max_value < dead_fly:
                max_value = dead_fly
    
    print(f'#{test_case}', max_value)