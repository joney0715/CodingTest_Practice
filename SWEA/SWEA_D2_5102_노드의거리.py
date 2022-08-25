from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    visit[node] = 1

    while queue:
        n = queue.popleft()

        for i in graph[n]:
            if not visit[i]:
                queue.append(i)
                visit[i] = visit[n] + 1

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    start, end = map(int, input().split())

    visit = [0] * (V+1)
    bfs(start)
    if visit[end] > 0:
        print('#{}'.format(tc), visit[end]-1)
    else:
        print('#{}'.format(tc), 0)