# 5432_쇠막대 자르기
# 2022-08-16

T = int(input())

for tc in range(1, T+1):
    l_list = list(input())
    cnt = 0
    for _ in l_list:
        cnt += 1
    answer = 0
    steel = 0
    i = 0
    while i < cnt:
        if l_list[i] == '(' and l_list[i+1] == ')':
            answer += steel
            i += 2
        elif l_list[i] == '(':
            steel += 1
            i += 1
        else:
            answer += 1
            steel -= 1
            i += 1

    print('#{}'.format(tc), answer)
