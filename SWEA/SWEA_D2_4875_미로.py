dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def find(y, x):
    visit[y][x] = True
    N_list[y][x] = '1'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N and 0 <= ny < N) and N_list[ny][nx] != '1':
            find(ny, nx)

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    N_list = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if N_list[i][j] == '2':
                start = (i, j)
            if N_list[i][j] == '3':
                end = (i, j)

    visit = [[False] * N for _ in range(N)]
    find(start[0], start[1])

    if visit[end[0]][end[1]]:
        print('#{}'.format(tc), 1)
    else:
        print('#{}'.format(tc), 0)