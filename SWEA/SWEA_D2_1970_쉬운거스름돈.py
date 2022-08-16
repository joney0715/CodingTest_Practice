
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    cash = [50000,10000,5000,1000,500,100,50,10]
    count = [0] * 8

    for i in range(8):
        count[i] += N // cash[i]
        N = N % cash[i]
    print('#{}'.format(tc))
    print(*count)
    
