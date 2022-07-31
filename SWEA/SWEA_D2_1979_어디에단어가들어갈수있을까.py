T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    maps = []
    for _ in range(N):
        mapping = list(map(int, input().split()))
        maps.append(mapping)
    # N, K = 5, 3
    # maps = [[0, 0, 1, 1, 1],[1, 1, 1, 1, 0],[0, 0, 1, 0, 0],[0, 1, 1, 1, 1],[1, 1, 1, 0, 1]]

    stack_1 = []
    stack_2 = []
    count = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 1:
                stack_1.append(maps[i][j])
            else:
                if len(stack_1) == K:
                    count += 1
                    stack_1.clear()
                else:
                    stack_1.clear()

            if maps[j][i] == 1:
                stack_2.append(maps[i][j])
            else:
                if len(stack_2) == K:
                    count += 1
                    stack_2.clear()
                else:
                    stack_2.clear()
        if len(stack_1) == K:
            count += 1
            stack_1.clear()
        else:
            stack_1.clear()
        if len(stack_2) == K:
            count += 1
            stack_2.clear()
        else:
            stack_2.clear()
    
    print(f'#{test_case}', count)
            