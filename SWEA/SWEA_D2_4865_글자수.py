# 4865_글자수
# 2022-08-16

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    answer = 0
    for char in str1:
        cnt = str2.count(char)
        if answer < cnt:
            answer = cnt
    
    print('#{}'.format(tc), answer)