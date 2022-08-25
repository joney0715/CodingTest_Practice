from collections import deque
import sys

sys.stdin = open('input_1226.txt', 'r')
input = sys.stdin.readline

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

            if (0 <= nr < 16 and 0 <= nc < 16) and maze[nr][nc] == '0':
                maze[nr][nc] = 'a'
                queue.append((nr, nc))
            if (0 <= nr < 16 and 0 <= nc < 16) and maze[nr][nc] == '3':
                return 1
    else:
        return 0

for _ in range(10):
    tc = int(input())

    maze = [list(input()) for _ in range(16)]

    print('#{}'.format(tc), find_route(1, 1))

