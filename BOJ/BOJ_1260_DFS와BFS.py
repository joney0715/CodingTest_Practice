from collections import deque

def dfs(node):
    visit[node] = True
    print(node, end=' ')
    graph[node].sort()
    for n in graph[node]:
        if not visit[n]:
            dfs(n)
    return True

def bfs(node):
    que = deque([node])
    visit[node] = True
    while que:
        n = que.popleft()
        print(n, end=' ')
        graph[n].sort()
        for i in graph[n]:
            if not visit[i]:
                que.append(i)
                visit[i] = True

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visit = [False] * (N+1)
dfs(V)
print()
visit = [False] * (N+1)
bfs(V)