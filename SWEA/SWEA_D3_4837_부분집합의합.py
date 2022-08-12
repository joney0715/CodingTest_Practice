# 4837_부분집합의 합
# 2022-08-11

T = int(input())

for tc in range(1, T+1):
    nums = list(range(1,13))
    N, K = map(int, input().split())

    n = 12
    count = 0
    for i in range(1, 1<<n):
        subset_sum = 0
        subset_count = 0        
        for j in range(n):
            if i & (1<<j):
                subset_count += 1
                subset_sum += nums[j]  
        
        if subset_count == N and subset_sum == K:
            count += 1
    else:
        print('#{}'.format(tc), count)