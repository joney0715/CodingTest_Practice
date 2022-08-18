# 2005_파스칼삼각형
# 2022-08-17

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    pascal = [[''] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if j == 0 or j == i:
                pascal[i][j] = 1
            elif 0 < j < i:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print('#{}'.format(tc))
    for row in pascal:
        print(*row)