from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

pipe = {
    1: [0,1,2,3],
    2: [1,3],
    3: [0,2],
    4: [1,2],
    5: [3,2],
    6: [3,0],
    7: [1,0]
}

def bfs(R, C):
    queue = deque()
    visit[R][C] = 1
    queue.append((R,C))

    while queue:
        y, x = queue.popleft()

        move = pipe[N_list[y][x]]
        for m in move:
            nx = x + dx[m]
            ny = y + dy[m]

            if 0 <= nx < M and 0 <= ny < N and not visit[ny][nx] and N_list[ny][nx] != 0:
                next_move = pipe[N_list[ny][nx]]
                for n in next_move:
                    nnx = nx + dx[n]
                    nny = ny + dy[n]
                    if nnx == x and nny == y:
                        queue.append((ny, nx))
                        visit[ny][nx] = visit[y][x] + 1


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())

    N_list = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * M for _ in range(N)]

    bfs(R, C)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visit[i][j] <= L:
                cnt += 1

    print('#{}'.format(tc), cnt)

