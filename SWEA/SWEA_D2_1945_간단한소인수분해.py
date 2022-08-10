
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    e = 0
    while not N % 11:
        N //= 11
        e += 1

    d = 0
    while not N % 7:
        N //= 7
        d += 1
    
    c = 0
    while not N % 5:
        N //= 5
        c += 1
    
    b = 0
    while not N % 3:
        N //= 3
        b += 1
    
    a = 0
    while not N % 2:
        N //= 2
        a += 1
    
    print('#{}'.format(tc), a, b, c, d, e)