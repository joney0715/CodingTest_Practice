import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def dfs(n, subset):
    if B <=sum(subset) <= sum(H_list):
        subsets.append(sum(subset) - B)
        return

    for i in range(n, N):
        dfs(i+1, subset+[H_list[i]])

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H_list = list(map(int, input().split()))

    subsets = []
    dfs(0, [])
    
    print('#{}'.format(tc), min(subsets))