T = int(input())

for _ in range(1, T+1):
    case, N = input().split()
    N = int(N)

    nums = input().split()

    rule = {
        'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4,
        'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9
    }

    nums = [rule.get(n) for n in nums]

    for i in range(N):
        idx = i
        for j in range(i+1, N):
            if nums[idx] > nums[j]:
                idx = j
        nums[i], nums[idx] = nums[idx], nums[i]

    rule = {value:key for key,value in rule.items()}
    nums = [rule.get(n) for n in nums]

    print(case)
    print(*nums)
