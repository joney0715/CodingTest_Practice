T = 10
for test_case in range(1, T + 1):
    N = int(input())
    buildings = list(map(int, input().split()))

    count = 0
    for i in range(N-2):
        if buildings[i]:
            if buildings[i] > buildings[i-1] and buildings[i] > buildings[i-2]:
                if buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2]:
                                        
                    h_max = buildings[i-2]
                    for h in [buildings[i-1], buildings[i+1], buildings[i+2]]:
                        if h_max < h:
                            h_max = h

                    count += buildings[i] - h_max
    
    print(f'#{test_case} {count}')