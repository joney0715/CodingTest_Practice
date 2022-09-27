from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def combinate(n, c):
    if len(c) == M:
        combination.append(c)
    
    for i in range(n, len(available)):
        if available[i] not in c:
            combinate(i+1, c+[available[i]])


def bfs(virus):
    k = 1000000
    queue = deque(virus)
    result = 0
    while queue:
        r, c = queue.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and not lab[nr][nc] and visit[nr][nc]==-1:
                visit[nr][nc] = visit[r][c] + 1
                result = max(visit[nr][nc], result)
                queue.append((nr, nc))
    
    for row in range(N):
        for col in range(N):
            if lab[row][col] == 0 and visit[row][col] == -1:
                result = 1000000

    return min(result, k)

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

available = []
for r in range(N):
    for c in range(N):
        if lab[r][c] == 2:
            available.append((r,c))
            lab[r][c] = 0

combination = []
combinate(0, [])

answer = []
for combi in combination:
    visit = [[-1]*N for _ in range(N)]
    for r,c in combi:
        visit[r][c] = 0
    result = bfs(combi)
    answer.append(result)


ans = min(answer)
if ans == 1000000:
    print(-1)
else:
    print(ans)