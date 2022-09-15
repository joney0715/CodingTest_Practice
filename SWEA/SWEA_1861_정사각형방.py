from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

def bfs(y, x):
    queue = deque()
    room_list = []

    queue.append((y, x))
    room_list.append(N_list[y][x])

    visited[y][x] = True
    while queue:
        cur_y, cur_x = queue.popleft()

        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]

            if 0 <= ny < N and 0 <= nx < N and abs(N_list[ny][nx] - N_list[cur_y][cur_x]) == 1 and not visited[ny][nx]:
                queue.append((ny, nx))
                room_list.append(N_list[ny][nx])
                visited[ny][nx] = True

    result = (len(room_list), min(room_list))
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    N_list = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    cnt = 0
    room = []
    for i in range(N):
        for j in range(N):
            result = bfs(i, j)
            room.append(result)
            
    room = sorted(room, key = lambda x : (-x[0], x[1]))

    print('#{}'.format(tc), room[0][1], room[0][0])