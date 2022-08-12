import sys

sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(sys.stdin.readline())

    ladder = [list(map(int, sys.stdin.readline().split())) for _ in range(100)]
    
    # 도착점에서 2가 있는 인덱스 검색
    idx = 0
    for i in range(100):       
        if ladder[99][i] == 2:
            idx = i

    # 거꾸로 거슬러 올라감
    y = 99
    while y >= 0:
        ladder[y][idx] = 2   

        if idx < 99 and ladder[y][idx+1] == 1:
            idx += 1
        elif idx > 0 and ladder[y][idx-1] == 1:
            idx -= 1
        else:
            y -= 1

        if not y:
            print('#{} {}'.format(tc, idx))