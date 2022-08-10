# 4834_숫자카드
# 2022-08-09

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = int(input())

    count = [0] *10
    while card:
        count[card % 10] += 1

        card //= 10

    idx_max = 0    
    for j in range(len(count)):   
        
        if count[idx_max] <= count[j]:
            idx_max = j

    
    print(f'#{tc}', idx_max, count[idx_max])