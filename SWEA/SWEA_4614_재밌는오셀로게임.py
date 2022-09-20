import sys
sys.stdin = open('sample_input(1).txt', 'r')
input = sys.stdin.readline

T = int(input())

dx = [1, 0, -1, 0, 1, -1, 1, -1]
dy = [0, 1, 0, -1, 1, -1, -1, 1]
d = {1: 2, 2: 1}

def function(x, y, c):
    N_list[x][y] = c
    for i in range(8):
        stack = []
        idx = 1
        nx = x + (idx * dx[i])
        ny = y + (idx * dy[i])

        while 0 <= nx < N and 0 <= ny < N:
            if N_list[nx][ny] == d.get(c):
                stack.append((nx, ny))
            elif N_list[nx][ny] == c and stack:
                while stack:
                    xx, yy = stack.pop()
                    N_list[xx][yy] = c
                break
            else:
                break

            idx += 1
            nx = x + (idx * dx[i])
            ny = y + (idx * dy[i])



for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_list = [[0] * N for _ in range(N)]

    N_list[N//2][N//2-1], N_list[N//2-1][N//2] = 1, 1
    N_list[N//2-1][N//2-1], N_list[N//2][N//2] = 2, 2

    for _ in range(M):
        x, y, c = map(int, input().split())
        x -= 1
        y -= 1
        function(x, y, c)

    black = white = 0
    for y in range(N):
        for x in range(N):
            if N_list[y][x] == 1:
                black += 1
            elif N_list[y][x] == 2:
                white += 1

    print('#{}'.format(tc), black, white)