T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    K_list = list(map(int, input().split()))

    answer = []
    for i in range(1, N+1):
        if i not in K_list:
            answer.append(i)
    print('#{}'.format(tc), *answer)
