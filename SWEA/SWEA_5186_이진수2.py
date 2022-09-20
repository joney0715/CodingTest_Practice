import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    answer = ''
    while N != 0:
        N = N * 2
        b = str(N)
        answer += b[0]
        N = N - int(N)

        if len(answer) >= 13:
            answer = 'overflow'
            break

    print('#{}'.format(tc), answer)
