# 4864_문자열 비교
# 2022-08-16

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    cnt = str2.count(str1)
    
    if cnt:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))