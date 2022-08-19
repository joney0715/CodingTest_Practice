import sys

sys.stdin = open('input.txt', 'r')

def route(node):
    visit[node] = True
    for n in graph[node]:
        if not visit[n]:
            route(n)

for _ in range(10):
    tc, N = map(int, sys.stdin.readline().split())
    N_list = list(map(int, sys.stdin.readline().split()))

    graph = [[] for _ in range(100)]

    i = j = 0    
    while i < N:
        graph[N_list[j]].append(N_list[j+1])
        i += 1
        j += 2
    
    visit = [False] * 100
    route(0)
    if visit[99]:
        print('#{}'.format(tc), 1)
    else:
        print('#{}'.format(tc), 0)


