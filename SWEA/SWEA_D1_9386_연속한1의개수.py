T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = input() + '0'

    count = 0
    answer = 0
    for i in range(N+1):
        if nums[i] == '1':
            count += 1
        else:
            if count > answer:
                answer = count
            count = 0
    print('#{}'.format(tc), answer)