import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    # 노드 개수, 리프 노드의 개수, 타겟 노드 번호
    N, M, L = map(int, input().split())

    nums = [0] * (N+2)
    for _ in range(M):
        n, num = map(int, input().split())
        nums[n] = num

    for i in range(N-M, 0, -1):
        nums[i] = nums[i*2] + nums[i*2+1]  

    print('#{}'.format(tc), nums[L])
