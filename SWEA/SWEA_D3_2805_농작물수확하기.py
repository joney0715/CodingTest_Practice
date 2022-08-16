T = int(input())

for tc in range(1, T+1):
    N = int(input())

    farm = []
    for _ in range(N):
        row = input()
        row = [int(i) for i in row]
        farm.append(row)
    
    value = 0
    for v in farm[N//2]:
        value += v
        
    for i in range(N//2):
        value += farm[i][(N//2)]
        value += farm[-i-1][(N//2)]
        for j in range(1,i+1):            
            value += farm[i][(N//2) + j]
            value += farm[i][(N//2) - j]
            value += farm[-i-1][(N//2) + j]
            value += farm[-i-1][(N//2) - j]
        
    print('#{}'.format(tc), value)
            