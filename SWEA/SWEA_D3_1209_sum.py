
T = 10

def N_sum(n_list):
    sum_value = 0
    for n in n_list:
        sum_value += n
    return sum_value

for _ in range(1, T+1):
    tc = int(input())

    N_list = [list(map(int, input().split())) for _ in range(100)]
    sum_values = []

    # 행
    for row in N_list:
        sum_value = N_sum(row)
        sum_values.append(sum_value)
        
    # 열
    for i in range(100):
        col = []
        for j in range(100):
            col.append(N_list[j][i])
        sum_value = N_sum(col)
        sum_values.append(sum_value)
    
    # 대각
    diagonal = []
    for k in range(100):
        diagonal.append(N_list[k][k])
    sum_value = N_sum(diagonal)
    sum_values.append(sum_value)

    diagonal = []
    for k in range(99,-1,-1):
        diagonal.append(N_list[k][k])
    sum_value = N_sum(diagonal)
    sum_values.append(sum_value)

    # 최대값
    max_value = 0
    for value in sum_values:
        if max_value < value:
            max_value = value
    
    print('#{}'.format(tc), max_value)