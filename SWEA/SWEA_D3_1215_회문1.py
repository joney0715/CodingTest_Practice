T = 10

for tc in range(1, T+1):
    k = int(input())
    mapping = [input() for _ in range(8)]

    cnt = 0
    for y1 in range(8):
        for x1 in range(8-k+1):
            if mapping[y1][x1:x1 + k] == mapping[y1][x1:x1 + k][::-1]:
                cnt += 1

    for x2 in range(8):
        for y2 in range(8-k+1):
            temp = ''
            for i in range(k):
                temp += mapping[y2+i][x2]
            if temp == temp[::-1]:
                cnt += 1

    print('#{}'.format(tc), cnt)