import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    M_bin = bin(M)[2:][::-1][0:N]

    if M_bin.count('1') == N:
        print('#{} ON'.format(tc))
    else:
        print('#{} OFF'.format(tc))         