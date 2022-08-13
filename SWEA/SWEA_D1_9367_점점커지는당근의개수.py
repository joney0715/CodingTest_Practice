T = int(input())

for tc in range(1, T+1):
    N = int(input())
    size = list(map(int, input().split()))
    size.append(0)

    count = 1
    answer = 1
    k = size[0]    
    for i in range(1, N+1):
        if k < size[i]:
            count += 1
        else:
            if answer < count:
                answer = count
            count = 1
        k = size[i]

    print('#{}'.format(tc), answer)