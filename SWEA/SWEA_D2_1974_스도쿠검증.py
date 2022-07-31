T = int(input())
for test_case in range(1, T + 1):
    matrix = []
    for i in range(9):
        row = list(map(int, input().split()))
        matrix.append(row)

    def row(matrix):
        for row in matrix:
            if len(row) != len(set(row)):
                return False
        return True

    def col(matrix):
        for i in range(9):
            m = [
                matrix[0][i],matrix[1][i],matrix[2][i],
                matrix[3][i],matrix[4][i],matrix[5][i],
                matrix[6][i],matrix[7][i],matrix[8][i]
            ]
            if len(m) != len(set(m)):
                return False
        return True  

    def grid(matrix):
        for n in range(0,7,3):
            for i in range(0,7,3):
                m = [
                    matrix[0+n][0+i],matrix[0+n][1+i],matrix[0+n][2+i],
                    matrix[1+n][0+i],matrix[1+n][1+i],matrix[1+n][2+i],
                    matrix[2+n][0+i],matrix[2+n][1+i],matrix[2+n][2+i]
                    ]                
                if len(m) != len(set(m)):
                    return False                   
        return True

    if (col(matrix) and row(matrix)) and grid(matrix):
        print(f'#{test_case}', 1)
    else:
        print(f'#{test_case}', 0)
