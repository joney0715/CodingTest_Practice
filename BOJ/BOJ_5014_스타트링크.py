from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    visit[start] = 1

    while queue:
        f = queue.popleft()

        if f == G:
            return

        for i in (f+U, f-D):
            if 0 < i <= F and not visit[i]:
                visit[i] = visit[f] + 1
                queue.append(i)


F, S, G, U, D = map(int, input().split())

visit = [False for _ in range(F+1)]
bfs(S)

if visit[G]:
    print(visit[G] - 1)
else:
    print('use the stairs')