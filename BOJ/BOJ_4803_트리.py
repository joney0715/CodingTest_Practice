import sys

def find_tree(pre_node, node):
    visit[node] = True

    for k in tree[node]:
        if pre_node == k:
            continue

        if visit[k]:
            return False

        result = find_tree(node, k)
        if not result:
            return False

    return True

testcase = 0
while True:
    testcase += 1
    N, M = sys.stdin.readline().split()
    N, M = int(N), int(M)
    if N == 0 and M == 0:
        break

    visit =[False] * (N+1)
    tree = [[] for _ in range(N+1)]

    for i in range(M):
        start, end = sys.stdin.readline().split()
        start, end = int(start), int(end)
        tree[start].append(end)
        tree[end].append(start)

    count = 0
    for j in range(1, N+1):
        if not visit[j]:
            if find_tree(0, j):
                count += 1                

    if count == 0:
        print(f'Case {testcase}: No trees.')
    elif count == 1:
        print(f'Case {testcase}: There is one tree.')
    else:
        print(f'Case {testcase}: A forest of {count} trees.')

# 단방향 트리로 했을 경우 틀림
# 반례
# 노드6 간선5
# 1 2
# 2 3
# 3 4
# 5 2
# 6 1
# 의 경우 사이클이 없는데도 트리가 아닌 경우가 되어버림
