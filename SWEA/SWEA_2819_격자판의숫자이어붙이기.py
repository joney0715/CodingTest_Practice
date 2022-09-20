import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(count, row, col, result):
    result += matrix[row][col]

    if count == 6:
        answer.add(result)
        return

    for d in range(4):
        nr = row + dr[d]
        nc = col + dc[d]

        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(count+1, nr, nc, result)

T = int(input())
for tc in range(1, T+1):
    matrix = [list(input().split()) for _ in range(4)]

    answer = set()
    for r in range(4):
        for c in range(4):
            dfs(0, r, c, '')
        
    print('#{}'.format(tc), len(answer))