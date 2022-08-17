T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    for i in range(N):
        for j in range(i+1, N):
            if scores[j] > scores[i]:
                scores[i], scores[j] = scores[j], scores[i]
            
    answer = 0
    for k in range(K):
        answer += scores[k]
    
    print('#{}'.format(tc), answer)