T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    for i in range(N-1):
        if i % 2:
            idx_min = i
            for j in range(i+1, N):
                if ai[idx_min] > ai[j]:
                    idx_min = j
            ai[i], ai[idx_min] = ai[idx_min], ai[i] 
        else:
            idx_max = i
            for j in range(i+1, N):
                if ai[idx_max] < ai[j]:
                    idx_max = j
            ai[i], ai[idx_max] = ai[idx_max], ai[i] 
        
    print('#{}'.format(tc), *ai[:10])