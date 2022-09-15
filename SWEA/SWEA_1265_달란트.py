import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    dal, n = map(int, input().split())
    s = dal // n
    r = dal % n

    a = (s+1)**r
    b = s**(n-r)
    print('#{}'.format(tc), a*b)