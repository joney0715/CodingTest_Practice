from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_route(row, col):
    queue = deque()
    queue.append((row, col))
    cnt = 0
    while queue:
        r, c = queue.popleft()

        for d in range(4):
            nr = r + dx[d]
            nc = c + dy[d]

            if (0 <= nr < N and 0 <= nc < N) and maze[nr][nc] == '0':
                if nr == end[0] and nc == end[1]:
                    cnt = maze[r][c]

                maze[nr][nc] = maze[r][c] + 1
                queue.append((nr, nc))
    return cnt

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    maze = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start = (i, j)
            if maze[i][j] == '3':
                end = (i, j)

    maze[start[0]][start[1]] = 0
    maze[end[0]][end[1]] = '0'
    cnt = find_route(start[0], start[1])

    print('#{}'.format(tc), cnt)

