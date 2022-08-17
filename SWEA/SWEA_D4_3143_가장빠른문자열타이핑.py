# 3143_가장 빠른 문자열 타이핑
# 2022-08-16

T = int(input())

for tc in range(1, T+1):
    A, B = input().split()

    A = A.replace(B,' ')

    count = 0
    for _ in A:
        count += 1

    print('#{}'.format(tc), count)
