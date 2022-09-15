from collections import defaultdict, deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def bfs(node):
    queue = deque()
    queue.append(node)

    while queue:
        n = queue.popleft()
        
        for i in graph[n]:
            if visit[i] == -1:
                visit[i] = visit[n] + 1
                queue.append(i)

T = 10
for tc in range(1, T+1):
    N, start = map(int, input().split())
    nums = list(map(int, input().split()))

    graph = defaultdict(set)
    i = 0
    while i+1 <= len(nums):
        graph[nums[i]].add(nums[i+1])
        i += 2

    visit = [-1] * (max(nums)+1)
    visit[start] = 0
    bfs(start)

    idx = []
    for j in range(len(visit)):
        if visit[j] == max(visit):
            idx.append(j)

    print('#{}'.format(tc), max(idx))
