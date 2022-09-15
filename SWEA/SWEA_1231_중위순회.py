from collections import defaultdict
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def inorder(node):
    global answer
    
    if len(tree[node]) > 0:
        inorder(tree[node][0])
    answer += alphabet[node]
    if len(tree[node]) == 2:
        inorder(tree[node][1])

T = 10
for tc in range(1, T+1):
    N = int(input())

    alphabet = [''] * (N+1)
    tree = defaultdict(list)
    for _ in range(N):
        i = input().split()
        alphabet[int(i[0])] = i[1]
        if len(i) > 2:
            tree[int(i[0])].append(int(i[2]))
        if len(i) > 3:
            tree[int(i[0])].append(int(i[3]))

    answer = ''
    inorder(list(tree)[0])
    print('#{}'.format(tc), answer)