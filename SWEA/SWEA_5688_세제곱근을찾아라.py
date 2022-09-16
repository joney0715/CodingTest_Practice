import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    answer = -1
    for i in range(1, N+1):
        if i ** 3 > N:
            break
        if i ** 3 == N:
            answer = i
            break 

    print('#{}'.format(tc), answer)