import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def inorder(node):
    global n

    if node <= N:
        inorder(2*node)
        n += 1
        tree[node] = n
        inorder(2*node+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [0 for _ in range(N+1)]
    n = 0
    inorder(1)
    
    print('#{}'.format(tc), tree[1], tree[N//2])