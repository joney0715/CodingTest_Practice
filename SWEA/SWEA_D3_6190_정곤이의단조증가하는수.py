T = int(input())

def increase(n):
    temp = 10
    while n:
        v = n % 10
        if v > temp:
            return False
        temp = v
        n = n // 10
    return True

for tc in range(1, T+1):
    N = int(input())

    N_list = list(map(int, input().split()))

    max_value = -1
    for i in range(N):
        for j in range(i+1,N):
            num = N_list[i] * N_list[j] 
            if increase(num):
                if max_value < num:
                    max_value = num
    print('#{}'.format(tc), max_value)