# 4871_그래프경로
# 2022-08-18

def find_route(node):
    visit[node] = True
    for n in graph[node]:
        if not visit[n]:
            find_route(n)

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)

    start, end = map(int, input().split())

    visit = [False] * (V+1)
    find_route(start)
    if visit[end]:
        print('#{}'.format(tc), 1)
    else:
        print('#{}'.format(tc), 0)
