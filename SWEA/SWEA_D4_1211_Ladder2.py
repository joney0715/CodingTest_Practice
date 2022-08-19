import sys

sys.stdin = open('input_1211.txt', 'r')

for _ in range(1, 11):
    tc = int(sys.stdin.readline())
    ladder = [list(map(int, sys.stdin.readline().split())) for _ in range(100)]

    min_value = 10000
    for i in range(100):
        if ladder[0][i]:
            visit= [[False] * 100 for _ in range(100)]
            cnt = 0
            j = 0
            idx = i
            while j < 100:
                cnt += 1
                visit[j][idx] = True
                if idx < 99 and ladder[j][idx+1] == 1 and not visit[j][idx+1]:
                    idx += 1
                elif idx > 0 and ladder[j][idx-1] == 1 and not visit[j][idx-1]:
                    idx -= 1
                else:
                    j += 1
    
            if min_value > cnt:
                min_value = cnt
                answer = i

    print('#{}'.format(tc), answer)