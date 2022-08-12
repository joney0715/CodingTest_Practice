# 1966_숫자를정렬하자
# 2022-08-11

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    for i in range(N):
        for j in range(i+1, N):
            if nums[j] < nums[i]:
                nums[j], nums[i] = nums[i], nums[j]

    print('#{}'.format(tc), *nums)