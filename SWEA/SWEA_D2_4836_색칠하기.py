# 4836_색칠하기
# 2022-08-11

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    mapping = [[0] *10 for _ in range(10)]
    area_list = [list(map(int, input().split())) for _ in range(N)]
    
    for area in area_list:

        for r in range(area[0], area[2]+1):
            for c in range(area[1], area[3]+1):
                if mapping[r][c] != area[4]:
                    mapping[r][c] += area[4]

    count = 0
    for row in range(10):
        for col in range(10):
            if mapping[row][col] == 3:
                count += 1

    print('#{}'.format(tc), count)


