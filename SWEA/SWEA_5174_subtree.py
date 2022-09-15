import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def count_node(node):
    global cnt

    if node == 0:
        return 

    cnt += 1
    count_node(left[node])
    count_node(right[node])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    nums = list(map(int, input().split()))

    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(0, len(nums), 2):
        if left[nums[i]]:
            right[nums[i]] = nums[i+1]
        else:
            left[nums[i]] = nums[i+1]

    cnt = 0
    count_node(N)

    print('#{}'.format(tc), cnt)