import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.insert(0,0)
    tree = [0]
    for i in range(1, N+1):
        tree.append(nums[i])
       
        if i != 0:
            k = i
            while k > 0:
                if tree[k] < tree[k // 2]:
                    tree[k], tree[k // 2] = tree[k // 2], tree[k]
                
                k = k // 2
    
    answer = 0
    while N > 0:
        N = N // 2
        answer += tree[N]
    
    print('#{}'.format(tc), answer)