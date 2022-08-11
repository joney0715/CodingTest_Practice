T = int(input())

d_row = [1, 0, -1 ,0]
d_col = [0, 1, 0, -1]

for tc in range(1, T+1):
    N = int(input())
    N_list = [[0]*N for _ in range(N)]
    
    k = 1
    direction = 0
    col = row = 0
    while k <= N**2:
        N_list[col][row] = k

        row_next = row + d_row[direction]
        col_next = col + d_col[direction]

        if row_next < 0 or row_next >= N or col_next < 0 or col_next >= N or N_list[col_next][row_next]:           
            direction += 1
            direction %= 4
            row += d_row[direction]
            col += d_col[direction]
            
        else:
            row += d_row[direction]
            col += d_col[direction]
        k += 1

    print('#{}'.format(tc))
    for row in N_list:
        print(*row) 