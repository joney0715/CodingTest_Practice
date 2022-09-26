from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(row, col):
    global flag
    changes = []
    cnt = 1
    popul = N_list[row][col]
    queue = deque()
    queue.append((row, col))
    visit[row][col] = True

    while queue:
        r, c = queue.popleft()
        changes.append((r, c))
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and not visit[nr][nc]:
                if L <= abs(N_list[nr][nc] - N_list[r][c]) <= R:
                    cnt += 1
                    visit[nr][nc] = True
                    popul += N_list[nr][nc]
                    queue.append((nr, nc))

    if cnt > 1:
        flag = 1
        move = popul // cnt
        for c in changes:
            N_list[c[0]][c[1]] = move


N, L, R = map(int, input().split())
N_list = [list(map(int, input().split())) for _ in range(N)]


answer = 0
while True:
    flag = 0
    visit = [[False]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visit[r][c]:
                bfs(r, c)

    if not flag:
        break

    answer += 1
        
print(answer)
