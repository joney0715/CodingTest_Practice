# 4861_회문
# 2022-08-16

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    string = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            if string[i][j:j + M] == string[i][j:j + M][::-1]:
                answer = string[i][j:j + M]
                break

    for i in range(N):
        for j in range(N-M+1):
            temp = ''
            for k in range(M):
                temp += string[j+k][i]
            if temp == temp[::-1]:
                answer = temp
                break

    print('#{} {}'.format(tc, answer))
